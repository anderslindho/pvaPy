// Copyright information and license terms for this software can be
// found in the file LICENSE that is included with the distribution

#include "boost/python/class.hpp"
#include "boost/python/overloads.hpp"
#include "boost/python/manage_new_object.hpp"
#include "RpcClient.h"

using namespace boost::python;

// 
// RPC Client class
// 
void wrapRpcClient()
{

class_<RpcClient>("RpcClient", 
    "RpcClient is a client class for PVA RPC services.\n\n"
#if defined PVA_RPC_API_VERSION && PVA_RPC_API_VERSION == 460
    "**RpcClient(channelName[, pvRequest])**\n\n"
    "\t:Parameter: *channelName* (str) - RPC service channel name\n\n"
    "\t:Parameter: *pvRequest* (PvObject) - pvRequest object specifying structure sent on creating RPC if default structure not used\n\n"
#else
    "**RpcClient(channelName)**\n\n"
    "\t:Parameter: *channelName* (str) - RPC service channel name\n\n"
#endif
    "\tThis example creates RPC client for channel 'createNtTable':\n\n"
    "\t::\n\n"
    "\t\trpcClient = RpcClient('createNtTable')\n\n", 
    init<std::string>())
#if defined PVA_RPC_API_VERSION && PVA_RPC_API_VERSION == 460
    .def(init<std::string, const PvObject&>())
#endif

    .def("getChannelName",
        &RpcClient::getChannelName,
        "Retrieves channel name.\n\n"
        ":Returns: channel name\n\n"
        "::\n\n"
        "    channelName = rpcClient.getChannelName()\n\n")

    .def("getTimeout",
        &RpcClient::getTimeout,
        "Retrieves client timeout.\n\n"
        ":Returns: client timeout in seconds\n\n"
        "::\n\n"
        "    timeout = rpcClient.getTimeout()\n\n")

    .def("setTimeout",
        &RpcClient::setTimeout,
        args("timeout"),
        "Sets client timeout.\n\n"
        ":Parameter: *timeout* (float) - client timeout in seconds\n\n"
        "::\n\n"
        "    client.setTimeout(10.0)\n\n")

    .def("invoke", 
        static_cast<PvObject*(RpcClient::*)(const PvObject&, double)>(&RpcClient::invoke),
        return_value_policy<manage_new_object>(), 
        args("pvArgument", "timeout"),
        "Invokes RPC call against service registered on the PV specified channel, and with a specified timeout.\n\n"
        ":Parameter: *pvArgument* (PvObject) - PV argument object with a structure conforming to requirements of the RPC service registered on the given PV channel\n\n"
        ":Parameter: *timeout* (float) - RPC client timeout in seconds\n\n"
        ":Returns: PV response object\n\n"
        "The following code works with the above RPC service example:\n\n"
        "::\n\n"
        "    pvArgument = PvObject({'nRows' : INT, 'nColumns' : INT})\n\n"
        "    pvArgument.set({'nRows' : 10, 'nColumns' : 10})\n\n"
        "    pvResponse = rpcClient(pvArgument, 10)\n\n"
        "    ntTable = NtTable(pvResponse)\n\n")

    .def("invoke", 
        static_cast<PvObject*(RpcClient::*)(const PvObject&)>(&RpcClient::invoke),
        return_value_policy<manage_new_object>(), 
        args("pvArgument"),
        "Invokes RPC call against service registered on the PV specified channel, with a timeout set previously (if not set, default timeout of 1 second will be used).\n\n"
        ":Parameter: *pvArgument* (PvObject) - PV argument object with a structure conforming to requirements of the RPC service registered on the given PV channel\n\n"
        ":Returns: PV response object\n\n"
        "The following code works with the above RPC service example:\n\n"
        "::\n\n"
        "    pvArgument = PvObject({'nRows' : INT, 'nColumns' : INT})\n\n"
        "    pvArgument.set({'nRows' : 10, 'nColumns' : 10})\n\n"
        "    pvResponse = rpcClient(pvArgument)\n\n"
        "    ntTable = NtTable(pvResponse)\n\n")
;

} // wrapRpcClient()

