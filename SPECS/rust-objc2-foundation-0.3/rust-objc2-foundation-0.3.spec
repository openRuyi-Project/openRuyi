# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/foundationerrors) = %{version}
Provides:       crate(%{pkgname}/foundationlegacyswiftcompatibility) = %{version}
Provides:       crate(%{pkgname}/nsaffinetransform) = %{version}
Provides:       crate(%{pkgname}/nsappleeventmanager) = %{version}
Provides:       crate(%{pkgname}/nsapplescript) = %{version}
Provides:       crate(%{pkgname}/nsarchiver) = %{version}
Provides:       crate(%{pkgname}/nsautoreleasepool) = %{version}
Provides:       crate(%{pkgname}/nsbackgroundactivityscheduler) = %{version}
Provides:       crate(%{pkgname}/nsbundle) = %{version}
Provides:       crate(%{pkgname}/nsbyteorder) = %{version}
Provides:       crate(%{pkgname}/nscache) = %{version}
Provides:       crate(%{pkgname}/nscalendardate) = %{version}
Provides:       crate(%{pkgname}/nscharacterset) = %{version}
Provides:       crate(%{pkgname}/nsclassdescription) = %{version}
Provides:       crate(%{pkgname}/nscoder) = %{version}
Provides:       crate(%{pkgname}/nscompoundpredicate) = %{version}
Provides:       crate(%{pkgname}/nsconnection) = %{version}
Provides:       crate(%{pkgname}/nsdate) = %{version}
Provides:       crate(%{pkgname}/nsdateformatter) = %{version}
Provides:       crate(%{pkgname}/nsdateinterval) = %{version}
Provides:       crate(%{pkgname}/nsdateintervalformatter) = %{version}
Provides:       crate(%{pkgname}/nsdebug) = %{version}
Provides:       crate(%{pkgname}/nsdecimal) = %{version}
Provides:       crate(%{pkgname}/nsdecimalnumber) = %{version}
Provides:       crate(%{pkgname}/nsdictionary) = %{version}
Provides:       crate(%{pkgname}/nsdistantobject) = %{version}
Provides:       crate(%{pkgname}/nsdistributedlock) = %{version}
Provides:       crate(%{pkgname}/nsenergyformatter) = %{version}
Provides:       crate(%{pkgname}/nsenumerator) = %{version}
Provides:       crate(%{pkgname}/nserror) = %{version}
Provides:       crate(%{pkgname}/nsexception) = %{version}
Provides:       crate(%{pkgname}/nsexpression) = %{version}
Provides:       crate(%{pkgname}/nsextensioncontext) = %{version}
Provides:       crate(%{pkgname}/nsextensionitem) = %{version}
Provides:       crate(%{pkgname}/nsextensionrequesthandling) = %{version}
Provides:       crate(%{pkgname}/nsfilehandle) = %{version}
Provides:       crate(%{pkgname}/nsfilepresenter) = %{version}
Provides:       crate(%{pkgname}/nsformatter) = %{version}
Provides:       crate(%{pkgname}/nsgarbagecollector) = %{version}
Provides:       crate(%{pkgname}/nshashtable) = %{version}
Provides:       crate(%{pkgname}/nshfsfiletypes) = %{version}
Provides:       crate(%{pkgname}/nshost) = %{version}
Provides:       crate(%{pkgname}/nshttpcookie) = %{version}
Provides:       crate(%{pkgname}/nshttpcookiestorage) = %{version}
Provides:       crate(%{pkgname}/nsindexpath) = %{version}
Provides:       crate(%{pkgname}/nsindexset) = %{version}
Provides:       crate(%{pkgname}/nsinflectionrule) = %{version}
Provides:       crate(%{pkgname}/nsinvocation) = %{version}
Provides:       crate(%{pkgname}/nskeyedarchiver) = %{version}
Provides:       crate(%{pkgname}/nskeyvaluecoding) = %{version}
Provides:       crate(%{pkgname}/nskeyvaluesharedobservers) = %{version}
Provides:       crate(%{pkgname}/nslengthformatter) = %{version}
Provides:       crate(%{pkgname}/nslistformatter) = %{version}
Provides:       crate(%{pkgname}/nslocale) = %{version}
Provides:       crate(%{pkgname}/nslocalizednumberformatrule) = %{version}
Provides:       crate(%{pkgname}/nslock) = %{version}
Provides:       crate(%{pkgname}/nsmaptable) = %{version}
Provides:       crate(%{pkgname}/nsmassformatter) = %{version}
Provides:       crate(%{pkgname}/nsmeasurement) = %{version}
Provides:       crate(%{pkgname}/nsmetadata) = %{version}
Provides:       crate(%{pkgname}/nsmetadataattributes) = %{version}
Provides:       crate(%{pkgname}/nsmethodsignature) = %{version}
Provides:       crate(%{pkgname}/nsmorphology) = %{version}
Provides:       crate(%{pkgname}/nsnotification) = %{version}
Provides:       crate(%{pkgname}/nsnull) = %{version}
Provides:       crate(%{pkgname}/nsnumberformatter) = %{version}
Provides:       crate(%{pkgname}/nsobject) = %{version}
Provides:       crate(%{pkgname}/nsobjectscripting) = %{version}
Provides:       crate(%{pkgname}/nsoperation) = %{version}
Provides:       crate(%{pkgname}/nsorderedcollectionchange) = %{version}
Provides:       crate(%{pkgname}/nsorderedset) = %{version}
Provides:       crate(%{pkgname}/nsorthography) = %{version}
Provides:       crate(%{pkgname}/nspersonnamecomponents) = %{version}
Provides:       crate(%{pkgname}/nspointerarray) = %{version}
Provides:       crate(%{pkgname}/nsportcoder) = %{version}
Provides:       crate(%{pkgname}/nsportmessage) = %{version}
Provides:       crate(%{pkgname}/nsportnameserver) = %{version}
Provides:       crate(%{pkgname}/nspredicate) = %{version}
Provides:       crate(%{pkgname}/nsprogress) = %{version}
Provides:       crate(%{pkgname}/nsprotocolchecker) = %{version}
Provides:       crate(%{pkgname}/nsproxy) = %{version}
Provides:       crate(%{pkgname}/nsrange) = %{version}
Provides:       crate(%{pkgname}/nsrelativedatetimeformatter) = %{version}
Provides:       crate(%{pkgname}/nsrunloop) = %{version}
Provides:       crate(%{pkgname}/nsscanner) = %{version}
Provides:       crate(%{pkgname}/nsscriptclassdescription) = %{version}
Provides:       crate(%{pkgname}/nsscriptcoercionhandler) = %{version}
Provides:       crate(%{pkgname}/nsscriptcommand) = %{version}
Provides:       crate(%{pkgname}/nsscriptcommanddescription) = %{version}
Provides:       crate(%{pkgname}/nsscriptexecutioncontext) = %{version}
Provides:       crate(%{pkgname}/nsscriptkeyvaluecoding) = %{version}
Provides:       crate(%{pkgname}/nsscriptobjectspecifiers) = %{version}
Provides:       crate(%{pkgname}/nsscriptstandardsuitecommands) = %{version}
Provides:       crate(%{pkgname}/nsscriptsuiteregistry) = %{version}
Provides:       crate(%{pkgname}/nsscriptwhosetests) = %{version}
Provides:       crate(%{pkgname}/nsset) = %{version}
Provides:       crate(%{pkgname}/nssortdescriptor) = %{version}
Provides:       crate(%{pkgname}/nsspellserver) = %{version}
Provides:       crate(%{pkgname}/nstask) = %{version}
Provides:       crate(%{pkgname}/nstermofaddress) = %{version}
Provides:       crate(%{pkgname}/nsthread) = %{version}
Provides:       crate(%{pkgname}/nstimer) = %{version}
Provides:       crate(%{pkgname}/nstimezone) = %{version}
Provides:       crate(%{pkgname}/nsubiquitouskeyvaluestore) = %{version}
Provides:       crate(%{pkgname}/nsundomanager) = %{version}
Provides:       crate(%{pkgname}/nsunit) = %{version}
Provides:       crate(%{pkgname}/nsurlauthenticationchallenge) = %{version}
Provides:       crate(%{pkgname}/nsurlcache) = %{version}
Provides:       crate(%{pkgname}/nsurlconnection) = %{version}
Provides:       crate(%{pkgname}/nsurlcredential) = %{version}
Provides:       crate(%{pkgname}/nsurlcredentialstorage) = %{version}
Provides:       crate(%{pkgname}/nsurldownload) = %{version}
Provides:       crate(%{pkgname}/nsurlerror) = %{version}
Provides:       crate(%{pkgname}/nsurlhandle) = %{version}
Provides:       crate(%{pkgname}/nsurlprotectionspace) = %{version}
Provides:       crate(%{pkgname}/nsurlprotocol) = %{version}
Provides:       crate(%{pkgname}/nsurlrequest) = %{version}
Provides:       crate(%{pkgname}/nsurlresponse) = %{version}
Provides:       crate(%{pkgname}/nsurlsession) = %{version}
Provides:       crate(%{pkgname}/nsuseractivity) = %{version}
Provides:       crate(%{pkgname}/nsuserdefaults) = %{version}
Provides:       crate(%{pkgname}/nsusernotification) = %{version}
Provides:       crate(%{pkgname}/nsuserscripttask) = %{version}
Provides:       crate(%{pkgname}/nsuuid) = %{version}
Provides:       crate(%{pkgname}/nsvalue) = %{version}
Provides:       crate(%{pkgname}/nsvaluetransformer) = %{version}
Provides:       crate(%{pkgname}/nsxmldocument) = %{version}
Provides:       crate(%{pkgname}/nsxmldtd) = %{version}
Provides:       crate(%{pkgname}/nsxmldtdnode) = %{version}
Provides:       crate(%{pkgname}/nsxmlelement) = %{version}
Provides:       crate(%{pkgname}/nsxmlnode) = %{version}
Provides:       crate(%{pkgname}/nsxmlparser) = %{version}
Provides:       crate(%{pkgname}/nszone) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}
Provides:       crate(%{pkgname}/unstable-mutation-return-null) = %{version}
Provides:       crate(%{pkgname}/unstable-static-nsstring) = %{version}

%description
Source code for takopackized Rust crate "objc2-foundation"

%package     -n %{name}+bitflags
Summary:        Bindings to the Foundation framework - feature "bitflags" and 37 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/nsappleeventdescriptor) = %{version}
Provides:       crate(%{pkgname}/nsarray) = %{version}
Provides:       crate(%{pkgname}/nsattributedstring) = %{version}
Provides:       crate(%{pkgname}/nsbytecountformatter) = %{version}
Provides:       crate(%{pkgname}/nscalendar) = %{version}
Provides:       crate(%{pkgname}/nscomparisonpredicate) = %{version}
Provides:       crate(%{pkgname}/nsdata) = %{version}
Provides:       crate(%{pkgname}/nsdatecomponentsformatter) = %{version}
Provides:       crate(%{pkgname}/nsdistributednotificationcenter) = %{version}
Provides:       crate(%{pkgname}/nsfilecoordinator) = %{version}
Provides:       crate(%{pkgname}/nsfilemanager) = %{version}
Provides:       crate(%{pkgname}/nsfileversion) = %{version}
Provides:       crate(%{pkgname}/nsfilewrapper) = %{version}
Provides:       crate(%{pkgname}/nsgeometry) = %{version}
Provides:       crate(%{pkgname}/nsiso8601dateformatter) = %{version}
Provides:       crate(%{pkgname}/nsitemprovider) = %{version}
Provides:       crate(%{pkgname}/nsjsonserialization) = %{version}
Provides:       crate(%{pkgname}/nskeyvalueobserving) = %{version}
Provides:       crate(%{pkgname}/nslinguistictagger) = %{version}
Provides:       crate(%{pkgname}/nsmeasurementformatter) = %{version}
Provides:       crate(%{pkgname}/nsnetservices) = %{version}
Provides:       crate(%{pkgname}/nsnotificationqueue) = %{version}
Provides:       crate(%{pkgname}/nsobjcruntime) = %{version}
Provides:       crate(%{pkgname}/nsorderedcollectiondifference) = %{version}
Provides:       crate(%{pkgname}/nspathutilities) = %{version}
Provides:       crate(%{pkgname}/nspersonnamecomponentsformatter) = %{version}
Provides:       crate(%{pkgname}/nspointerfunctions) = %{version}
Provides:       crate(%{pkgname}/nsport) = %{version}
Provides:       crate(%{pkgname}/nsprocessinfo) = %{version}
Provides:       crate(%{pkgname}/nspropertylist) = %{version}
Provides:       crate(%{pkgname}/nsregularexpression) = %{version}
Provides:       crate(%{pkgname}/nsstream) = %{version}
Provides:       crate(%{pkgname}/nsstring) = %{version}
Provides:       crate(%{pkgname}/nstextcheckingresult) = %{version}
Provides:       crate(%{pkgname}/nsurl) = %{version}
Provides:       crate(%{pkgname}/nsxmlnodeoptions) = %{version}
Provides:       crate(%{pkgname}/nsxpcconnection) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSAppleEventDescriptor", "NSArray", "NSAttributedString", "NSByteCountFormatter", "NSCalendar", "NSComparisonPredicate", "NSData", "NSDateComponentsFormatter", "NSDistributedNotificationCenter", "NSFileCoordinator", "NSFileManager", "NSFileVersion", "NSFileWrapper", "NSGeometry", "NSISO8601DateFormatter", "NSItemProvider", "NSJSONSerialization", "NSKeyValueObserving", "NSLinguisticTagger", "NSMeasurementFormatter", "NSNetServices", "NSNotificationQueue", "NSObjCRuntime", "NSOrderedCollectionDifference", "NSPathUtilities", "NSPersonNameComponentsFormatter", "NSPointerFunctions", "NSPort", "NSProcessInfo", "NSPropertyList", "NSRegularExpression", "NSStream", "NSString", "NSTextCheckingResult", "NSURL", "NSXMLNodeOptions", and "NSXPCConnection" features.

%package     -n %{name}+block2
Summary:        Bindings to the Foundation framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the Foundation framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/foundationerrors) = %{version}
Requires:       crate(%{pkgname}/foundationlegacyswiftcompatibility) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/nsaffinetransform) = %{version}
Requires:       crate(%{pkgname}/nsappleeventdescriptor) = %{version}
Requires:       crate(%{pkgname}/nsappleeventmanager) = %{version}
Requires:       crate(%{pkgname}/nsapplescript) = %{version}
Requires:       crate(%{pkgname}/nsarchiver) = %{version}
Requires:       crate(%{pkgname}/nsarray) = %{version}
Requires:       crate(%{pkgname}/nsattributedstring) = %{version}
Requires:       crate(%{pkgname}/nsautoreleasepool) = %{version}
Requires:       crate(%{pkgname}/nsbackgroundactivityscheduler) = %{version}
Requires:       crate(%{pkgname}/nsbundle) = %{version}
Requires:       crate(%{pkgname}/nsbytecountformatter) = %{version}
Requires:       crate(%{pkgname}/nsbyteorder) = %{version}
Requires:       crate(%{pkgname}/nscache) = %{version}
Requires:       crate(%{pkgname}/nscalendar) = %{version}
Requires:       crate(%{pkgname}/nscalendardate) = %{version}
Requires:       crate(%{pkgname}/nscharacterset) = %{version}
Requires:       crate(%{pkgname}/nsclassdescription) = %{version}
Requires:       crate(%{pkgname}/nscoder) = %{version}
Requires:       crate(%{pkgname}/nscomparisonpredicate) = %{version}
Requires:       crate(%{pkgname}/nscompoundpredicate) = %{version}
Requires:       crate(%{pkgname}/nsconnection) = %{version}
Requires:       crate(%{pkgname}/nsdata) = %{version}
Requires:       crate(%{pkgname}/nsdate) = %{version}
Requires:       crate(%{pkgname}/nsdatecomponentsformatter) = %{version}
Requires:       crate(%{pkgname}/nsdateformatter) = %{version}
Requires:       crate(%{pkgname}/nsdateinterval) = %{version}
Requires:       crate(%{pkgname}/nsdateintervalformatter) = %{version}
Requires:       crate(%{pkgname}/nsdebug) = %{version}
Requires:       crate(%{pkgname}/nsdecimal) = %{version}
Requires:       crate(%{pkgname}/nsdecimalnumber) = %{version}
Requires:       crate(%{pkgname}/nsdictionary) = %{version}
Requires:       crate(%{pkgname}/nsdistantobject) = %{version}
Requires:       crate(%{pkgname}/nsdistributedlock) = %{version}
Requires:       crate(%{pkgname}/nsdistributednotificationcenter) = %{version}
Requires:       crate(%{pkgname}/nsenergyformatter) = %{version}
Requires:       crate(%{pkgname}/nsenumerator) = %{version}
Requires:       crate(%{pkgname}/nserror) = %{version}
Requires:       crate(%{pkgname}/nsexception) = %{version}
Requires:       crate(%{pkgname}/nsexpression) = %{version}
Requires:       crate(%{pkgname}/nsextensioncontext) = %{version}
Requires:       crate(%{pkgname}/nsextensionitem) = %{version}
Requires:       crate(%{pkgname}/nsextensionrequesthandling) = %{version}
Requires:       crate(%{pkgname}/nsfilecoordinator) = %{version}
Requires:       crate(%{pkgname}/nsfilehandle) = %{version}
Requires:       crate(%{pkgname}/nsfilemanager) = %{version}
Requires:       crate(%{pkgname}/nsfilepresenter) = %{version}
Requires:       crate(%{pkgname}/nsfileversion) = %{version}
Requires:       crate(%{pkgname}/nsfilewrapper) = %{version}
Requires:       crate(%{pkgname}/nsformatter) = %{version}
Requires:       crate(%{pkgname}/nsgarbagecollector) = %{version}
Requires:       crate(%{pkgname}/nsgeometry) = %{version}
Requires:       crate(%{pkgname}/nshashtable) = %{version}
Requires:       crate(%{pkgname}/nshfsfiletypes) = %{version}
Requires:       crate(%{pkgname}/nshost) = %{version}
Requires:       crate(%{pkgname}/nshttpcookie) = %{version}
Requires:       crate(%{pkgname}/nshttpcookiestorage) = %{version}
Requires:       crate(%{pkgname}/nsindexpath) = %{version}
Requires:       crate(%{pkgname}/nsindexset) = %{version}
Requires:       crate(%{pkgname}/nsinflectionrule) = %{version}
Requires:       crate(%{pkgname}/nsinvocation) = %{version}
Requires:       crate(%{pkgname}/nsiso8601dateformatter) = %{version}
Requires:       crate(%{pkgname}/nsitemprovider) = %{version}
Requires:       crate(%{pkgname}/nsjsonserialization) = %{version}
Requires:       crate(%{pkgname}/nskeyedarchiver) = %{version}
Requires:       crate(%{pkgname}/nskeyvaluecoding) = %{version}
Requires:       crate(%{pkgname}/nskeyvalueobserving) = %{version}
Requires:       crate(%{pkgname}/nskeyvaluesharedobservers) = %{version}
Requires:       crate(%{pkgname}/nslengthformatter) = %{version}
Requires:       crate(%{pkgname}/nslinguistictagger) = %{version}
Requires:       crate(%{pkgname}/nslistformatter) = %{version}
Requires:       crate(%{pkgname}/nslocale) = %{version}
Requires:       crate(%{pkgname}/nslocalizednumberformatrule) = %{version}
Requires:       crate(%{pkgname}/nslock) = %{version}
Requires:       crate(%{pkgname}/nsmaptable) = %{version}
Requires:       crate(%{pkgname}/nsmassformatter) = %{version}
Requires:       crate(%{pkgname}/nsmeasurement) = %{version}
Requires:       crate(%{pkgname}/nsmeasurementformatter) = %{version}
Requires:       crate(%{pkgname}/nsmetadata) = %{version}
Requires:       crate(%{pkgname}/nsmetadataattributes) = %{version}
Requires:       crate(%{pkgname}/nsmethodsignature) = %{version}
Requires:       crate(%{pkgname}/nsmorphology) = %{version}
Requires:       crate(%{pkgname}/nsnetservices) = %{version}
Requires:       crate(%{pkgname}/nsnotification) = %{version}
Requires:       crate(%{pkgname}/nsnotificationqueue) = %{version}
Requires:       crate(%{pkgname}/nsnull) = %{version}
Requires:       crate(%{pkgname}/nsnumberformatter) = %{version}
Requires:       crate(%{pkgname}/nsobjcruntime) = %{version}
Requires:       crate(%{pkgname}/nsobject) = %{version}
Requires:       crate(%{pkgname}/nsobjectscripting) = %{version}
Requires:       crate(%{pkgname}/nsoperation) = %{version}
Requires:       crate(%{pkgname}/nsorderedcollectionchange) = %{version}
Requires:       crate(%{pkgname}/nsorderedcollectiondifference) = %{version}
Requires:       crate(%{pkgname}/nsorderedset) = %{version}
Requires:       crate(%{pkgname}/nsorthography) = %{version}
Requires:       crate(%{pkgname}/nspathutilities) = %{version}
Requires:       crate(%{pkgname}/nspersonnamecomponents) = %{version}
Requires:       crate(%{pkgname}/nspersonnamecomponentsformatter) = %{version}
Requires:       crate(%{pkgname}/nspointerarray) = %{version}
Requires:       crate(%{pkgname}/nspointerfunctions) = %{version}
Requires:       crate(%{pkgname}/nsport) = %{version}
Requires:       crate(%{pkgname}/nsportcoder) = %{version}
Requires:       crate(%{pkgname}/nsportmessage) = %{version}
Requires:       crate(%{pkgname}/nsportnameserver) = %{version}
Requires:       crate(%{pkgname}/nspredicate) = %{version}
Requires:       crate(%{pkgname}/nsprocessinfo) = %{version}
Requires:       crate(%{pkgname}/nsprogress) = %{version}
Requires:       crate(%{pkgname}/nspropertylist) = %{version}
Requires:       crate(%{pkgname}/nsprotocolchecker) = %{version}
Requires:       crate(%{pkgname}/nsproxy) = %{version}
Requires:       crate(%{pkgname}/nsrange) = %{version}
Requires:       crate(%{pkgname}/nsregularexpression) = %{version}
Requires:       crate(%{pkgname}/nsrelativedatetimeformatter) = %{version}
Requires:       crate(%{pkgname}/nsrunloop) = %{version}
Requires:       crate(%{pkgname}/nsscanner) = %{version}
Requires:       crate(%{pkgname}/nsscriptclassdescription) = %{version}
Requires:       crate(%{pkgname}/nsscriptcoercionhandler) = %{version}
Requires:       crate(%{pkgname}/nsscriptcommand) = %{version}
Requires:       crate(%{pkgname}/nsscriptcommanddescription) = %{version}
Requires:       crate(%{pkgname}/nsscriptexecutioncontext) = %{version}
Requires:       crate(%{pkgname}/nsscriptkeyvaluecoding) = %{version}
Requires:       crate(%{pkgname}/nsscriptobjectspecifiers) = %{version}
Requires:       crate(%{pkgname}/nsscriptstandardsuitecommands) = %{version}
Requires:       crate(%{pkgname}/nsscriptsuiteregistry) = %{version}
Requires:       crate(%{pkgname}/nsscriptwhosetests) = %{version}
Requires:       crate(%{pkgname}/nsset) = %{version}
Requires:       crate(%{pkgname}/nssortdescriptor) = %{version}
Requires:       crate(%{pkgname}/nsspellserver) = %{version}
Requires:       crate(%{pkgname}/nsstream) = %{version}
Requires:       crate(%{pkgname}/nsstring) = %{version}
Requires:       crate(%{pkgname}/nstask) = %{version}
Requires:       crate(%{pkgname}/nstermofaddress) = %{version}
Requires:       crate(%{pkgname}/nstextcheckingresult) = %{version}
Requires:       crate(%{pkgname}/nsthread) = %{version}
Requires:       crate(%{pkgname}/nstimer) = %{version}
Requires:       crate(%{pkgname}/nstimezone) = %{version}
Requires:       crate(%{pkgname}/nsubiquitouskeyvaluestore) = %{version}
Requires:       crate(%{pkgname}/nsundomanager) = %{version}
Requires:       crate(%{pkgname}/nsunit) = %{version}
Requires:       crate(%{pkgname}/nsurl) = %{version}
Requires:       crate(%{pkgname}/nsurlauthenticationchallenge) = %{version}
Requires:       crate(%{pkgname}/nsurlcache) = %{version}
Requires:       crate(%{pkgname}/nsurlconnection) = %{version}
Requires:       crate(%{pkgname}/nsurlcredential) = %{version}
Requires:       crate(%{pkgname}/nsurlcredentialstorage) = %{version}
Requires:       crate(%{pkgname}/nsurldownload) = %{version}
Requires:       crate(%{pkgname}/nsurlerror) = %{version}
Requires:       crate(%{pkgname}/nsurlhandle) = %{version}
Requires:       crate(%{pkgname}/nsurlprotectionspace) = %{version}
Requires:       crate(%{pkgname}/nsurlprotocol) = %{version}
Requires:       crate(%{pkgname}/nsurlrequest) = %{version}
Requires:       crate(%{pkgname}/nsurlresponse) = %{version}
Requires:       crate(%{pkgname}/nsurlsession) = %{version}
Requires:       crate(%{pkgname}/nsuseractivity) = %{version}
Requires:       crate(%{pkgname}/nsuserdefaults) = %{version}
Requires:       crate(%{pkgname}/nsusernotification) = %{version}
Requires:       crate(%{pkgname}/nsuserscripttask) = %{version}
Requires:       crate(%{pkgname}/nsuuid) = %{version}
Requires:       crate(%{pkgname}/nsvalue) = %{version}
Requires:       crate(%{pkgname}/nsvaluetransformer) = %{version}
Requires:       crate(%{pkgname}/nsxmldocument) = %{version}
Requires:       crate(%{pkgname}/nsxmldtd) = %{version}
Requires:       crate(%{pkgname}/nsxmldtdnode) = %{version}
Requires:       crate(%{pkgname}/nsxmlelement) = %{version}
Requires:       crate(%{pkgname}/nsxmlnode) = %{version}
Requires:       crate(%{pkgname}/nsxmlnodeoptions) = %{version}
Requires:       crate(%{pkgname}/nsxmlparser) = %{version}
Requires:       crate(%{pkgname}/nsxpcconnection) = %{version}
Requires:       crate(%{pkgname}/nszone) = %{version}
Requires:       crate(%{pkgname}/objc2-core-foundation) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-7
Summary:        Bindings to the Foundation framework - feature "gnustep-1-7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-1-7) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-1-7) >= 0.6.2
Requires:       crate(objc2-0.6/std) >= 0.6.2
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-8
Summary:        Bindings to the Foundation framework - feature "gnustep-1-8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-7) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-1-8) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-1-8) >= 0.6.2
Requires:       crate(objc2-0.6/std) >= 0.6.2
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-9
Summary:        Bindings to the Foundation framework - feature "gnustep-1-9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-8) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-1-9) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-1-9) >= 0.6.2
Requires:       crate(objc2-0.6/std) >= 0.6.2
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Bindings to the Foundation framework - feature "gnustep-2-0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-9) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-2-0) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-2-0) >= 0.6.2
Requires:       crate(objc2-0.6/std) >= 0.6.2
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Bindings to the Foundation framework - feature "gnustep-2-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-2-0) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-2-1) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-2-1) >= 0.6.2
Requires:       crate(objc2-0.6/std) >= 0.6.2
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the Foundation framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Bindings to the Foundation framework - feature "objc2-core-foundation"
Requires:       crate(%{pkgname}) = %{version}
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
Provides:       crate(%{pkgname}/objc2-core-foundation) = %{version}

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-services
Summary:        Bindings to the Foundation framework - feature "objc2-core-services"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-services-0.3/ae) >= 0.3.2
Requires:       crate(objc2-core-services-0.3/aedatamodel) >= 0.3.2
Requires:       crate(objc2-core-services-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-services) = %{version}

%description -n %{name}+objc2-core-services
This metapackage enables feature "objc2-core-services" for the Rust objc2-foundation crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
