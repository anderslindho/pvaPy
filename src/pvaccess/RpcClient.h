// Copyright information and license terms for this software can be
// found in the file LICENSE that is included with the distribution

#ifndef RPC_CLIENT_H
#define RPC_CLIENT_H

#include <string>

#include "PvaClient.h"
#include "PvObject.h"
#include "pv/event.h" // this should really be in pv/rpcClient.h
#include "pv/rpcClient.h"

/**
 * RPC client for PV access.
 */
class RpcClient : public PvaClient
{
public:
    static const int DefaultTimeout;

    RpcClient(const std::string& channelName);
#if defined PVA_RPC_API_VERSION && PVA_RPC_API_VERSION >= 460
    RpcClient(const std::string& channelName, const PvObject& pvRequestObject);
#endif
    RpcClient(const RpcClient& pvaRpcClient);
    std::string getChannelName() const;
    double getTimeout() const;
    void setTimeout(double);

    virtual ~RpcClient();
    epics::pvData::PVStructurePtr request(const epics::pvData::PVStructurePtr& pvRequest, double timeout=DefaultTimeout);
    // For some reason default argument does not work with boost overloading.
    PvObject* invoke(const PvObject& pvArgumentObject, double timeout);
    PvObject* invoke(const PvObject& pvArgumentObject);

private:
    static epics::pvAccess::RPCClient::shared_pointer createRpcClient(const std::string& channelName, const epics::pvData::PVStructurePtr& pvRequest, double timeout=DefaultTimeout);
    epics::pvAccess::RPCClient::shared_pointer getRpcClient(const epics::pvData::PVStructurePtr& pvRequest, double timeout=DefaultTimeout);

    bool rpcClientInitialized;
    epics::pvAccess::RPCClient::shared_pointer rpcClient;
    std::string channelName;
    epics::pvData::PVStructure::shared_pointer pvRequest;
    double timeout;
};

inline std::string RpcClient::getChannelName() const
{
    return channelName;
}

inline double RpcClient::getTimeout() const
{
    return timeout;
}

inline void RpcClient::setTimeout(double timeout) 
{
    this->timeout = timeout;
}

#endif
