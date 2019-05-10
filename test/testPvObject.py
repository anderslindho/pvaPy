#!/usr/bin/env python

from pvaccess import PvObject
from pvaccess import PvInt
from pvaccess import PvString
from pvaccess import PvFloat
from pvaccess import PvDouble
from pvaccess import BOOLEAN
from pvaccess import BYTE
from pvaccess import UBYTE
from pvaccess import SHORT
from pvaccess import USHORT
from pvaccess import INT
from pvaccess import UINT
from pvaccess import LONG
from pvaccess import ULONG
from pvaccess import FLOAT
from pvaccess import DOUBLE
from pvaccess import STRING
from testUtility import TestUtility

class TestPvObject:

    #
    # Boolean 
    #

    def test_Boolean(self):
        value = TestUtility.getRandomBoolean()
        pv = PvObject({'v' : BOOLEAN}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomBoolean()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomBoolean()
        pv.setBoolean(value)
        assert(pv.getBoolean() == value)

    #
    # Byte
    #

    def test_Byte(self):
        value = chr(TestUtility.getRandomUByte())
        pv = PvObject({'v' : BYTE}, {'v' : value})
        assert(pv['v'] == value)
        value = chr(TestUtility.getRandomUByte())
        pv['v'] = value 
        assert(pv['v'] == value)
        value = chr(TestUtility.getRandomUByte())
        pv.setByte(value)
        assert(pv.getByte() == value)
     
    #
    # UByte
    #

    def test_UByte(self):
        value = TestUtility.getRandomUByte()
        pv = PvObject({'v' : UBYTE}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomUByte()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomUByte()
        pv.setUByte(value)
        assert(pv.getUByte() == value)
     
    #
    # Short
    #

    def test_Short(self):
        value = TestUtility.getRandomShort()
        pv = PvObject({'v' : SHORT}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomShort()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomShort()
        pv.setShort(value)
        assert(pv.getShort() == value)
     
    #
    # UShort
    #

    def test_UShort(self):
        value = TestUtility.getRandomUShort()
        pv = PvObject({'v' : USHORT}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomUShort()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomUShort()
        pv.setUShort(value)
        assert(pv.getUShort() == value)
     
    #
    # Int
    #

    def test_Int(self):
        value = TestUtility.getRandomInt()
        pv = PvObject({'v' : INT}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomInt()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomInt()
        pv.setInt(value)
        assert(pv.getInt() == value)
     
    #
    # UInt
    #

    def test_UInt(self):
        value = TestUtility.getRandomUInt()
        pv = PvObject({'v' : UINT}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomUInt()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomUInt()
        pv.setUInt(value)
        assert(pv.getUInt() == value)
     
    #
    # Long
    #

    def test_Long(self):
        value = TestUtility.getRandomLong()
        pv = PvObject({'v' : LONG}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomLong()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomLong()
        pv.setLong(value)
        assert(pv.getLong() == value)
     
    #
    # ULong
    #

    def test_ULong(self):
        value = TestUtility.getRandomULong()
        pv = PvObject({'v' : ULONG}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomULong()
        pv['v'] = value 
        assert(pv['v'] == value)
        value = TestUtility.getRandomULong()
        pv.setULong(value)
        assert(pv.getULong() == value)
     
    #
    # Float
    #

    def test_Float(self):
        value = TestUtility.getRandomFloat()
        pv = PvObject({'v' : FLOAT}, {'v' : value})
        TestUtility.assertFloatEquality(pv['v'], value)
        value = TestUtility.getRandomFloat()
        pv['v'] = value 
        TestUtility.assertFloatEquality(pv['v'], value)
        value = TestUtility.getRandomFloat()
        pv.setFloat(value)
        TestUtility.assertFloatEquality(pv.getFloat(), value)
     
    #
    # Double
    #

    def test_Double(self):
        value = TestUtility.getRandomDouble()
        pv = PvObject({'v' : DOUBLE}, {'v' : value})
        TestUtility.assertDoubleEquality(pv['v'], value)
        value = TestUtility.getRandomDouble()
        pv['v'] = value 
        TestUtility.assertDoubleEquality(pv['v'], value)
        value = TestUtility.getRandomDouble()
        pv.setDouble(value)
        TestUtility.assertDoubleEquality(pv.getDouble(), value)
     
    #
    # String
    #

    def test_String(self):
        value = TestUtility.getRandomString()
        pv = PvObject({'v' : STRING}, {'v' : value})
        assert(pv['v'] == value)
        value = TestUtility.getRandomString()
        pv['v'] = value
        assert(pv['v'] == value)
        value = TestUtility.getRandomString()
        pv.setString(value)
        assert(pv.getString() == value)
     
    #
    # Scalar array
    #

    def test_ScalarArray(self):
        value = TestUtility.getRandomInt()
        size = TestUtility.getRandomListSize()
        valueList = [value]*size
        pv = PvObject({'vl' : [INT]}, {'vl' : valueList})
        vl = pv['vl']
        assert(len(vl) == len(valueList))
        assert(vl[0] == valueList[0])
        assert(vl[-1] == valueList[-1])

        value = TestUtility.getRandomInt()
        size = TestUtility.getRandomListSize()
        valueList = [value]*size
        pv['vl'] = valueList
        vl = pv['vl']
        assert(len(vl) == len(valueList))
        assert(vl[0] == valueList[0])
        assert(vl[-1] == valueList[-1])

        value = TestUtility.getRandomInt()
        size = TestUtility.getRandomListSize()
        valueList = [value]*size
        pv.setScalarArray(valueList)
        vl = pv.getScalarArray()
        assert(len(vl) == len(valueList))
        assert(vl[0] == valueList[0])
        assert(vl[-1] == valueList[-1])

    #
    # Variant Union
    #

    def test_VariantUnion(self):
        value = TestUtility.getRandomInt()
        pv = PvObject({'v' : ()}, {'v' : PvInt(value)})
        u = pv['v'][0]
        assert(u['value'] == value)
 
        value = TestUtility.getRandomString()
        pv['v'] = PvString(value)
        u = pv['v'][0]
        assert(u['value'] == value)

        value = TestUtility.getRandomFloat()
        pv.setUnion(PvFloat(value))
        u = pv['v'][0]
        TestUtility.assertFloatEquality(u['value'],value)

    #
    # Restricted Union
    #

    def test_RestrictedUnion(self):
        value = TestUtility.getRandomInt()
        unionPv = PvObject({'i':INT},{'i':value})
        pv = PvObject({'v' : ({'i':INT, 'f':FLOAT, 's':STRING},)}, {'v' : unionPv})
        u = pv['v'][0]
        assert(u['i'] == value)

        value = TestUtility.getRandomString()
        unionPv = PvObject({'s':STRING},{'s':value})
        pv['v'] = unionPv
        u = pv['v'][0]
        assert(u['s'] == value)
 
        value = TestUtility.getRandomFloat()
        unionPv = PvObject({'f':FLOAT},{'f':value})
        pv.setUnion(unionPv)
        u = pv['v'][0]
        TestUtility.assertFloatEquality(u['f'],value)
 
    #
    # Variant Union Array
    #

    def test_VariantUnionArray(self):
        size = TestUtility.getRandomListSize()
        pv = PvObject({'v' : [()]})
        unionList = []
        for i in range(0,size):
            value = TestUtility.getRandomInt()
            unionList.append(PvInt(value))
 
        pv['v'] = unionList
        ul = pv['v']
        for i in range(0,size):
            uli = ul[i][0]
            assert(uli['value'] == unionList[i]['value'])

        unionList.reverse()
        pv.setUnionArray(unionList)
        ul = pv.getUnionArray()
        for i in range(0,size):
            uli = ul[i]
            assert(uli['value'] == unionList[i]['value'])

    #
    #
    # Restricted Union Array
    #

    def test_RestrictedUnionArray(self):
        size = TestUtility.getRandomListSize()
        pv = PvObject({'v' : [({'i':INT,'s':STRING,'d':DOUBLE},)]})
        unionList = []
        for i in range(0,size):
            if i%3 == 0:
                value = TestUtility.getRandomInt()
                unionList.append(PvObject({'i':INT},{'i':value}))
            elif i%3 == 1:
                value = TestUtility.getRandomString()
                unionList.append(PvObject({'s':STRING},{'s':value}))
            else:
                value = TestUtility.getRandomDouble()
                unionList.append(PvObject({'d':DOUBLE},{'d':value}))
 
        pv['v'] = unionList
        ul = pv['v']
        for i in range(0,size):
            uli = ul[i][0]
            if 'i' in uli:
                assert(uli['i'] == unionList[i]['i'])
            elif 's' in uli:
                assert(uli['s'] == unionList[i]['s'])
            else:
                TestUtility.assertDoubleEquality(uli['d'],unionList[i]['d'])

        unionList.reverse()
        pv.setUnionArray(unionList)
        ul = pv['v']
        for i in range(0,size):
            uli = ul[i][0]
            if 'i' in uli:
                assert(uli['i'] == unionList[i]['i'])
            elif 's' in uli:
                assert(uli['s'] == unionList[i]['s'])
            else:
                TestUtility.assertDoubleEquality(uli['d'],unionList[i]['d'])

    #
    #
    # Structure
    #

    def test_Structure(self):
        pv = PvObject({
            's': STRING,
            'i': INT,
            'ru': ({'i' : INT, 'd' : DOUBLE, 's' : STRING},),
            'vu': (),
            'st': {'i' : INT, 'd' : DOUBLE, 's' : STRING},
        })
        value = TestUtility.getRandomString()
        pv['s'] = value
        assert(pv['s'] == value)

        value = TestUtility.getRandomInt()
        pv['i'] = value
        assert(pv['i'] == value)

        value = TestUtility.getRandomInt()
        unionPv = PvObject({'i':INT},{'i':value})
        pv['ru'] = unionPv
        u = pv['ru'][0]
        assert(u['i'] == value)

        value = TestUtility.getRandomString()
        pv['vu'] = PvString(value)
        u = pv['vu'][0]
        assert(u['value'] == value)

        value = TestUtility.getRandomInt()
        pv['st.i'] = value
        assert(pv['st.i'] == value)


    #
    #
    # Structure Array
    #

    def test_StructureArray(self):
        STRUCTURE = {
            's': STRING,
            'i': INT,
            'ru': ({'i' : INT, 'd' : DOUBLE, 's' : STRING},),
            'vu': (),
            'st': {'i' : INT, 'd' : DOUBLE, 's' : STRING},
        }
        size = TestUtility.getRandomListSize()
        pv = PvObject({'v':[STRUCTURE]})
        structureList = []
        for i in range(0,size):
            pv2 = PvObject(STRUCTURE)
            value = TestUtility.getRandomString()
            pv2['s'] = value

            value = TestUtility.getRandomInt()
            pv2['i'] = value

            value = TestUtility.getRandomInt()
            unionPv = PvObject({'i':INT},{'i':value})
            pv2['ru'] = unionPv

            value = TestUtility.getRandomString()
            pv2['vu'] = PvString(value)

            value = TestUtility.getRandomInt()
            pv2['st.i'] = value
            value = TestUtility.getRandomString()
            pv2['st.s'] = value
            value = TestUtility.getRandomDouble()
            pv2['st.d'] = value
       
            structureList.append(pv2)
        pv['v'] = structureList

        sa = pv['v']
        for i in range(0,size):
            pv2 = sa[i]
            assert(pv2['s'] == structureList[i]['s'])
            assert(pv2['i'] == structureList[i]['i'])
            ru = pv2['ru'][0] 
            assert(ru['i'] == structureList[i]['ru'][0]['i'])
            vu = pv2['vu'][0] 
            assert(vu['value'] == structureList[i]['vu'][0]['value'])
            assert(pv2['st']['i'] == structureList[i]['st.i'])
            assert(pv2['st']['s'] == structureList[i]['st.s'])
            assert(pv2['st']['d'] == structureList[i]['st.d'])
       

