# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-foundation
%global full_version 0.3.2
%global pkgname objc2-foundation-0.3

Name:           rust-objc2-foundation-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-foundation"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e3e0adef53c21f888deb4fa59fc59f7eb17404926ee8a6f59f5df0fd7f9f3272
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/foundationerrors)
Provides:       crate(%{pkgname}/foundationlegacyswiftcompatibility)
Provides:       crate(%{pkgname}/nsaffinetransform)
Provides:       crate(%{pkgname}/nsappleeventmanager)
Provides:       crate(%{pkgname}/nsapplescript)
Provides:       crate(%{pkgname}/nsarchiver)
Provides:       crate(%{pkgname}/nsautoreleasepool)
Provides:       crate(%{pkgname}/nsbackgroundactivityscheduler)
Provides:       crate(%{pkgname}/nsbundle)
Provides:       crate(%{pkgname}/nsbyteorder)
Provides:       crate(%{pkgname}/nscache)
Provides:       crate(%{pkgname}/nscalendardate)
Provides:       crate(%{pkgname}/nscharacterset)
Provides:       crate(%{pkgname}/nsclassdescription)
Provides:       crate(%{pkgname}/nscoder)
Provides:       crate(%{pkgname}/nscompoundpredicate)
Provides:       crate(%{pkgname}/nsconnection)
Provides:       crate(%{pkgname}/nsdate)
Provides:       crate(%{pkgname}/nsdateformatter)
Provides:       crate(%{pkgname}/nsdateinterval)
Provides:       crate(%{pkgname}/nsdateintervalformatter)
Provides:       crate(%{pkgname}/nsdebug)
Provides:       crate(%{pkgname}/nsdecimal)
Provides:       crate(%{pkgname}/nsdecimalnumber)
Provides:       crate(%{pkgname}/nsdictionary)
Provides:       crate(%{pkgname}/nsdistantobject)
Provides:       crate(%{pkgname}/nsdistributedlock)
Provides:       crate(%{pkgname}/nsenergyformatter)
Provides:       crate(%{pkgname}/nsenumerator)
Provides:       crate(%{pkgname}/nserror)
Provides:       crate(%{pkgname}/nsexception)
Provides:       crate(%{pkgname}/nsexpression)
Provides:       crate(%{pkgname}/nsextensioncontext)
Provides:       crate(%{pkgname}/nsextensionitem)
Provides:       crate(%{pkgname}/nsextensionrequesthandling)
Provides:       crate(%{pkgname}/nsfilehandle)
Provides:       crate(%{pkgname}/nsfilepresenter)
Provides:       crate(%{pkgname}/nsformatter)
Provides:       crate(%{pkgname}/nsgarbagecollector)
Provides:       crate(%{pkgname}/nshfsfiletypes)
Provides:       crate(%{pkgname}/nshttpcookie)
Provides:       crate(%{pkgname}/nshttpcookiestorage)
Provides:       crate(%{pkgname}/nshashtable)
Provides:       crate(%{pkgname}/nshost)
Provides:       crate(%{pkgname}/nsindexpath)
Provides:       crate(%{pkgname}/nsindexset)
Provides:       crate(%{pkgname}/nsinflectionrule)
Provides:       crate(%{pkgname}/nsinvocation)
Provides:       crate(%{pkgname}/nskeyvaluecoding)
Provides:       crate(%{pkgname}/nskeyvaluesharedobservers)
Provides:       crate(%{pkgname}/nskeyedarchiver)
Provides:       crate(%{pkgname}/nslengthformatter)
Provides:       crate(%{pkgname}/nslistformatter)
Provides:       crate(%{pkgname}/nslocale)
Provides:       crate(%{pkgname}/nslocalizednumberformatrule)
Provides:       crate(%{pkgname}/nslock)
Provides:       crate(%{pkgname}/nsmaptable)
Provides:       crate(%{pkgname}/nsmassformatter)
Provides:       crate(%{pkgname}/nsmeasurement)
Provides:       crate(%{pkgname}/nsmetadata)
Provides:       crate(%{pkgname}/nsmetadataattributes)
Provides:       crate(%{pkgname}/nsmethodsignature)
Provides:       crate(%{pkgname}/nsmorphology)
Provides:       crate(%{pkgname}/nsnotification)
Provides:       crate(%{pkgname}/nsnull)
Provides:       crate(%{pkgname}/nsnumberformatter)
Provides:       crate(%{pkgname}/nsobject)
Provides:       crate(%{pkgname}/nsobjectscripting)
Provides:       crate(%{pkgname}/nsoperation)
Provides:       crate(%{pkgname}/nsorderedcollectionchange)
Provides:       crate(%{pkgname}/nsorderedset)
Provides:       crate(%{pkgname}/nsorthography)
Provides:       crate(%{pkgname}/nspersonnamecomponents)
Provides:       crate(%{pkgname}/nspointerarray)
Provides:       crate(%{pkgname}/nsportcoder)
Provides:       crate(%{pkgname}/nsportmessage)
Provides:       crate(%{pkgname}/nsportnameserver)
Provides:       crate(%{pkgname}/nspredicate)
Provides:       crate(%{pkgname}/nsprogress)
Provides:       crate(%{pkgname}/nsprotocolchecker)
Provides:       crate(%{pkgname}/nsproxy)
Provides:       crate(%{pkgname}/nsrange)
Provides:       crate(%{pkgname}/nsrelativedatetimeformatter)
Provides:       crate(%{pkgname}/nsrunloop)
Provides:       crate(%{pkgname}/nsscanner)
Provides:       crate(%{pkgname}/nsscriptclassdescription)
Provides:       crate(%{pkgname}/nsscriptcoercionhandler)
Provides:       crate(%{pkgname}/nsscriptcommand)
Provides:       crate(%{pkgname}/nsscriptcommanddescription)
Provides:       crate(%{pkgname}/nsscriptexecutioncontext)
Provides:       crate(%{pkgname}/nsscriptkeyvaluecoding)
Provides:       crate(%{pkgname}/nsscriptobjectspecifiers)
Provides:       crate(%{pkgname}/nsscriptstandardsuitecommands)
Provides:       crate(%{pkgname}/nsscriptsuiteregistry)
Provides:       crate(%{pkgname}/nsscriptwhosetests)
Provides:       crate(%{pkgname}/nsset)
Provides:       crate(%{pkgname}/nssortdescriptor)
Provides:       crate(%{pkgname}/nsspellserver)
Provides:       crate(%{pkgname}/nstask)
Provides:       crate(%{pkgname}/nstermofaddress)
Provides:       crate(%{pkgname}/nsthread)
Provides:       crate(%{pkgname}/nstimezone)
Provides:       crate(%{pkgname}/nstimer)
Provides:       crate(%{pkgname}/nsurlauthenticationchallenge)
Provides:       crate(%{pkgname}/nsurlcache)
Provides:       crate(%{pkgname}/nsurlconnection)
Provides:       crate(%{pkgname}/nsurlcredential)
Provides:       crate(%{pkgname}/nsurlcredentialstorage)
Provides:       crate(%{pkgname}/nsurldownload)
Provides:       crate(%{pkgname}/nsurlerror)
Provides:       crate(%{pkgname}/nsurlhandle)
Provides:       crate(%{pkgname}/nsurlprotectionspace)
Provides:       crate(%{pkgname}/nsurlprotocol)
Provides:       crate(%{pkgname}/nsurlrequest)
Provides:       crate(%{pkgname}/nsurlresponse)
Provides:       crate(%{pkgname}/nsurlsession)
Provides:       crate(%{pkgname}/nsuuid)
Provides:       crate(%{pkgname}/nsubiquitouskeyvaluestore)
Provides:       crate(%{pkgname}/nsundomanager)
Provides:       crate(%{pkgname}/nsunit)
Provides:       crate(%{pkgname}/nsuseractivity)
Provides:       crate(%{pkgname}/nsuserdefaults)
Provides:       crate(%{pkgname}/nsusernotification)
Provides:       crate(%{pkgname}/nsuserscripttask)
Provides:       crate(%{pkgname}/nsvalue)
Provides:       crate(%{pkgname}/nsvaluetransformer)
Provides:       crate(%{pkgname}/nsxmldtd)
Provides:       crate(%{pkgname}/nsxmldtdnode)
Provides:       crate(%{pkgname}/nsxmldocument)
Provides:       crate(%{pkgname}/nsxmlelement)
Provides:       crate(%{pkgname}/nsxmlnode)
Provides:       crate(%{pkgname}/nsxmlparser)
Provides:       crate(%{pkgname}/nszone)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)
Provides:       crate(%{pkgname}/unstable-mutation-return-null)
Provides:       crate(%{pkgname}/unstable-static-nsstring)

%description
Source code for takopackized Rust crate "objc2-foundation"

%package     -n %{name}+bitflags
Summary:        Bindings to the Foundation framework - feature "bitflags" and 37 more
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/std) >= 2.11.0
Provides:       crate(%{pkgname}/bitflags)
Provides:       crate(%{pkgname}/nsappleeventdescriptor)
Provides:       crate(%{pkgname}/nsarray)
Provides:       crate(%{pkgname}/nsattributedstring)
Provides:       crate(%{pkgname}/nsbytecountformatter)
Provides:       crate(%{pkgname}/nscalendar)
Provides:       crate(%{pkgname}/nscomparisonpredicate)
Provides:       crate(%{pkgname}/nsdata)
Provides:       crate(%{pkgname}/nsdatecomponentsformatter)
Provides:       crate(%{pkgname}/nsdistributednotificationcenter)
Provides:       crate(%{pkgname}/nsfilecoordinator)
Provides:       crate(%{pkgname}/nsfilemanager)
Provides:       crate(%{pkgname}/nsfileversion)
Provides:       crate(%{pkgname}/nsfilewrapper)
Provides:       crate(%{pkgname}/nsgeometry)
Provides:       crate(%{pkgname}/nsiso8601dateformatter)
Provides:       crate(%{pkgname}/nsitemprovider)
Provides:       crate(%{pkgname}/nsjsonserialization)
Provides:       crate(%{pkgname}/nskeyvalueobserving)
Provides:       crate(%{pkgname}/nslinguistictagger)
Provides:       crate(%{pkgname}/nsmeasurementformatter)
Provides:       crate(%{pkgname}/nsnetservices)
Provides:       crate(%{pkgname}/nsnotificationqueue)
Provides:       crate(%{pkgname}/nsobjcruntime)
Provides:       crate(%{pkgname}/nsorderedcollectiondifference)
Provides:       crate(%{pkgname}/nspathutilities)
Provides:       crate(%{pkgname}/nspersonnamecomponentsformatter)
Provides:       crate(%{pkgname}/nspointerfunctions)
Provides:       crate(%{pkgname}/nsport)
Provides:       crate(%{pkgname}/nsprocessinfo)
Provides:       crate(%{pkgname}/nspropertylist)
Provides:       crate(%{pkgname}/nsregularexpression)
Provides:       crate(%{pkgname}/nsstream)
Provides:       crate(%{pkgname}/nsstring)
Provides:       crate(%{pkgname}/nstextcheckingresult)
Provides:       crate(%{pkgname}/nsurl)
Provides:       crate(%{pkgname}/nsxmlnodeoptions)
Provides:       crate(%{pkgname}/nsxpcconnection)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSAppleEventDescriptor", "NSArray", "NSAttributedString", "NSByteCountFormatter", "NSCalendar", "NSComparisonPredicate", "NSData", "NSDateComponentsFormatter", "NSDistributedNotificationCenter", "NSFileCoordinator", "NSFileManager", "NSFileVersion", "NSFileWrapper", "NSGeometry", "NSISO8601DateFormatter", "NSItemProvider", "NSJSONSerialization", "NSKeyValueObserving", "NSLinguisticTagger", "NSMeasurementFormatter", "NSNetServices", "NSNotificationQueue", "NSObjCRuntime", "NSOrderedCollectionDifference", "NSPathUtilities", "NSPersonNameComponentsFormatter", "NSPointerFunctions", "NSPort", "NSProcessInfo", "NSPropertyList", "NSRegularExpression", "NSStream", "NSString", "NSTextCheckingResult", "NSURL", "NSXMLNodeOptions", and "NSXPCConnection" features.

%package     -n %{name}+block2
Summary:        Bindings to the Foundation framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.2
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the Foundation framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/foundationerrors)
Requires:       crate(%{pkgname}/foundationlegacyswiftcompatibility)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/nsaffinetransform)
Requires:       crate(%{pkgname}/nsappleeventdescriptor)
Requires:       crate(%{pkgname}/nsappleeventmanager)
Requires:       crate(%{pkgname}/nsapplescript)
Requires:       crate(%{pkgname}/nsarchiver)
Requires:       crate(%{pkgname}/nsarray)
Requires:       crate(%{pkgname}/nsattributedstring)
Requires:       crate(%{pkgname}/nsautoreleasepool)
Requires:       crate(%{pkgname}/nsbackgroundactivityscheduler)
Requires:       crate(%{pkgname}/nsbundle)
Requires:       crate(%{pkgname}/nsbytecountformatter)
Requires:       crate(%{pkgname}/nsbyteorder)
Requires:       crate(%{pkgname}/nscache)
Requires:       crate(%{pkgname}/nscalendar)
Requires:       crate(%{pkgname}/nscalendardate)
Requires:       crate(%{pkgname}/nscharacterset)
Requires:       crate(%{pkgname}/nsclassdescription)
Requires:       crate(%{pkgname}/nscoder)
Requires:       crate(%{pkgname}/nscomparisonpredicate)
Requires:       crate(%{pkgname}/nscompoundpredicate)
Requires:       crate(%{pkgname}/nsconnection)
Requires:       crate(%{pkgname}/nsdata)
Requires:       crate(%{pkgname}/nsdate)
Requires:       crate(%{pkgname}/nsdatecomponentsformatter)
Requires:       crate(%{pkgname}/nsdateformatter)
Requires:       crate(%{pkgname}/nsdateinterval)
Requires:       crate(%{pkgname}/nsdateintervalformatter)
Requires:       crate(%{pkgname}/nsdebug)
Requires:       crate(%{pkgname}/nsdecimal)
Requires:       crate(%{pkgname}/nsdecimalnumber)
Requires:       crate(%{pkgname}/nsdictionary)
Requires:       crate(%{pkgname}/nsdistantobject)
Requires:       crate(%{pkgname}/nsdistributedlock)
Requires:       crate(%{pkgname}/nsdistributednotificationcenter)
Requires:       crate(%{pkgname}/nsenergyformatter)
Requires:       crate(%{pkgname}/nsenumerator)
Requires:       crate(%{pkgname}/nserror)
Requires:       crate(%{pkgname}/nsexception)
Requires:       crate(%{pkgname}/nsexpression)
Requires:       crate(%{pkgname}/nsextensioncontext)
Requires:       crate(%{pkgname}/nsextensionitem)
Requires:       crate(%{pkgname}/nsextensionrequesthandling)
Requires:       crate(%{pkgname}/nsfilecoordinator)
Requires:       crate(%{pkgname}/nsfilehandle)
Requires:       crate(%{pkgname}/nsfilemanager)
Requires:       crate(%{pkgname}/nsfilepresenter)
Requires:       crate(%{pkgname}/nsfileversion)
Requires:       crate(%{pkgname}/nsfilewrapper)
Requires:       crate(%{pkgname}/nsformatter)
Requires:       crate(%{pkgname}/nsgarbagecollector)
Requires:       crate(%{pkgname}/nsgeometry)
Requires:       crate(%{pkgname}/nshashtable)
Requires:       crate(%{pkgname}/nshfsfiletypes)
Requires:       crate(%{pkgname}/nshost)
Requires:       crate(%{pkgname}/nshttpcookie)
Requires:       crate(%{pkgname}/nshttpcookiestorage)
Requires:       crate(%{pkgname}/nsindexpath)
Requires:       crate(%{pkgname}/nsindexset)
Requires:       crate(%{pkgname}/nsinflectionrule)
Requires:       crate(%{pkgname}/nsinvocation)
Requires:       crate(%{pkgname}/nsiso8601dateformatter)
Requires:       crate(%{pkgname}/nsitemprovider)
Requires:       crate(%{pkgname}/nsjsonserialization)
Requires:       crate(%{pkgname}/nskeyedarchiver)
Requires:       crate(%{pkgname}/nskeyvaluecoding)
Requires:       crate(%{pkgname}/nskeyvalueobserving)
Requires:       crate(%{pkgname}/nskeyvaluesharedobservers)
Requires:       crate(%{pkgname}/nslengthformatter)
Requires:       crate(%{pkgname}/nslinguistictagger)
Requires:       crate(%{pkgname}/nslistformatter)
Requires:       crate(%{pkgname}/nslocale)
Requires:       crate(%{pkgname}/nslocalizednumberformatrule)
Requires:       crate(%{pkgname}/nslock)
Requires:       crate(%{pkgname}/nsmaptable)
Requires:       crate(%{pkgname}/nsmassformatter)
Requires:       crate(%{pkgname}/nsmeasurement)
Requires:       crate(%{pkgname}/nsmeasurementformatter)
Requires:       crate(%{pkgname}/nsmetadata)
Requires:       crate(%{pkgname}/nsmetadataattributes)
Requires:       crate(%{pkgname}/nsmethodsignature)
Requires:       crate(%{pkgname}/nsmorphology)
Requires:       crate(%{pkgname}/nsnetservices)
Requires:       crate(%{pkgname}/nsnotification)
Requires:       crate(%{pkgname}/nsnotificationqueue)
Requires:       crate(%{pkgname}/nsnull)
Requires:       crate(%{pkgname}/nsnumberformatter)
Requires:       crate(%{pkgname}/nsobjcruntime)
Requires:       crate(%{pkgname}/nsobject)
Requires:       crate(%{pkgname}/nsobjectscripting)
Requires:       crate(%{pkgname}/nsoperation)
Requires:       crate(%{pkgname}/nsorderedcollectionchange)
Requires:       crate(%{pkgname}/nsorderedcollectiondifference)
Requires:       crate(%{pkgname}/nsorderedset)
Requires:       crate(%{pkgname}/nsorthography)
Requires:       crate(%{pkgname}/nspathutilities)
Requires:       crate(%{pkgname}/nspersonnamecomponents)
Requires:       crate(%{pkgname}/nspersonnamecomponentsformatter)
Requires:       crate(%{pkgname}/nspointerarray)
Requires:       crate(%{pkgname}/nspointerfunctions)
Requires:       crate(%{pkgname}/nsport)
Requires:       crate(%{pkgname}/nsportcoder)
Requires:       crate(%{pkgname}/nsportmessage)
Requires:       crate(%{pkgname}/nsportnameserver)
Requires:       crate(%{pkgname}/nspredicate)
Requires:       crate(%{pkgname}/nsprocessinfo)
Requires:       crate(%{pkgname}/nsprogress)
Requires:       crate(%{pkgname}/nspropertylist)
Requires:       crate(%{pkgname}/nsprotocolchecker)
Requires:       crate(%{pkgname}/nsproxy)
Requires:       crate(%{pkgname}/nsrange)
Requires:       crate(%{pkgname}/nsregularexpression)
Requires:       crate(%{pkgname}/nsrelativedatetimeformatter)
Requires:       crate(%{pkgname}/nsrunloop)
Requires:       crate(%{pkgname}/nsscanner)
Requires:       crate(%{pkgname}/nsscriptclassdescription)
Requires:       crate(%{pkgname}/nsscriptcoercionhandler)
Requires:       crate(%{pkgname}/nsscriptcommand)
Requires:       crate(%{pkgname}/nsscriptcommanddescription)
Requires:       crate(%{pkgname}/nsscriptexecutioncontext)
Requires:       crate(%{pkgname}/nsscriptkeyvaluecoding)
Requires:       crate(%{pkgname}/nsscriptobjectspecifiers)
Requires:       crate(%{pkgname}/nsscriptstandardsuitecommands)
Requires:       crate(%{pkgname}/nsscriptsuiteregistry)
Requires:       crate(%{pkgname}/nsscriptwhosetests)
Requires:       crate(%{pkgname}/nsset)
Requires:       crate(%{pkgname}/nssortdescriptor)
Requires:       crate(%{pkgname}/nsspellserver)
Requires:       crate(%{pkgname}/nsstream)
Requires:       crate(%{pkgname}/nsstring)
Requires:       crate(%{pkgname}/nstask)
Requires:       crate(%{pkgname}/nstermofaddress)
Requires:       crate(%{pkgname}/nstextcheckingresult)
Requires:       crate(%{pkgname}/nsthread)
Requires:       crate(%{pkgname}/nstimer)
Requires:       crate(%{pkgname}/nstimezone)
Requires:       crate(%{pkgname}/nsubiquitouskeyvaluestore)
Requires:       crate(%{pkgname}/nsundomanager)
Requires:       crate(%{pkgname}/nsunit)
Requires:       crate(%{pkgname}/nsurl)
Requires:       crate(%{pkgname}/nsurlauthenticationchallenge)
Requires:       crate(%{pkgname}/nsurlcache)
Requires:       crate(%{pkgname}/nsurlconnection)
Requires:       crate(%{pkgname}/nsurlcredential)
Requires:       crate(%{pkgname}/nsurlcredentialstorage)
Requires:       crate(%{pkgname}/nsurldownload)
Requires:       crate(%{pkgname}/nsurlerror)
Requires:       crate(%{pkgname}/nsurlhandle)
Requires:       crate(%{pkgname}/nsurlprotectionspace)
Requires:       crate(%{pkgname}/nsurlprotocol)
Requires:       crate(%{pkgname}/nsurlrequest)
Requires:       crate(%{pkgname}/nsurlresponse)
Requires:       crate(%{pkgname}/nsurlsession)
Requires:       crate(%{pkgname}/nsuseractivity)
Requires:       crate(%{pkgname}/nsuserdefaults)
Requires:       crate(%{pkgname}/nsusernotification)
Requires:       crate(%{pkgname}/nsuserscripttask)
Requires:       crate(%{pkgname}/nsuuid)
Requires:       crate(%{pkgname}/nsvalue)
Requires:       crate(%{pkgname}/nsvaluetransformer)
Requires:       crate(%{pkgname}/nsxmldocument)
Requires:       crate(%{pkgname}/nsxmldtd)
Requires:       crate(%{pkgname}/nsxmldtdnode)
Requires:       crate(%{pkgname}/nsxmlelement)
Requires:       crate(%{pkgname}/nsxmlnode)
Requires:       crate(%{pkgname}/nsxmlnodeoptions)
Requires:       crate(%{pkgname}/nsxmlparser)
Requires:       crate(%{pkgname}/nsxpcconnection)
Requires:       crate(%{pkgname}/nszone)
Requires:       crate(%{pkgname}/objc2-core-foundation)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-7
Summary:        Bindings to the Foundation framework - feature "gnustep-1-7"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.2
Requires:       crate(block2-0.6/gnustep-1-7) >= 0.6.2
Requires:       crate(objc2-0.6/gnustep-1-7) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-1-7)

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-8
Summary:        Bindings to the Foundation framework - feature "gnustep-1-8"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-7)
Requires:       crate(block2-0.6/alloc) >= 0.6.2
Requires:       crate(block2-0.6/gnustep-1-8) >= 0.6.2
Requires:       crate(objc2-0.6/gnustep-1-8) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-1-8)

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-9
Summary:        Bindings to the Foundation framework - feature "gnustep-1-9"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-8)
Requires:       crate(block2-0.6/alloc) >= 0.6.2
Requires:       crate(block2-0.6/gnustep-1-9) >= 0.6.2
Requires:       crate(objc2-0.6/gnustep-1-9) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-1-9)

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Bindings to the Foundation framework - feature "gnustep-2-0"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-9)
Requires:       crate(block2-0.6/alloc) >= 0.6.2
Requires:       crate(block2-0.6/gnustep-2-0) >= 0.6.2
Requires:       crate(objc2-0.6/gnustep-2-0) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-2-0)

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Bindings to the Foundation framework - feature "gnustep-2-1"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-2-0)
Requires:       crate(block2-0.6/alloc) >= 0.6.2
Requires:       crate(block2-0.6/gnustep-2-1) >= 0.6.2
Requires:       crate(objc2-0.6/gnustep-2-1) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-2-1)

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the Foundation framework - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.184
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Bindings to the Foundation framework - feature "objc2-core-foundation"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfattributedstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcalendar) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcharacterset) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cffilesecurity) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cflocale) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfmachport) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfmessageport) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfset) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstream) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-foundation)

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-services
Summary:        Bindings to the Foundation framework - feature "objc2-core-services"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-services-0.3/ae) >= 0.3.2
Requires:       crate(objc2-core-services-0.3/aedatamodel) >= 0.3.2
Requires:       crate(objc2-core-services-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-services)

%description -n %{name}+objc2-core-services
This metapackage enables feature "objc2-core-services" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
