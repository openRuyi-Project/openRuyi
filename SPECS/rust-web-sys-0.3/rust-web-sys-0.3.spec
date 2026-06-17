# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name web-sys
%global full_version 0.3.98
%global pkgname web-sys-0.3

Name:           rust-web-sys-0.3
Version:        0.3.98
Release:        %autorelease
Summary:        Rust crate "web-sys"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/web-sys/index.html
#!RemoteAsset:  sha256:4b572dff8bcf38bad0fa19729c89bb5748b2b9b1d8be70cf90df697e3a8f32aa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3) >= 0.3.98
Requires:       crate(wasm-bindgen-0.2) >= 0.2.121
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/abortcontroller) = %{version}
Provides:       crate(%{pkgname}/abortsignal) = %{version}
Provides:       crate(%{pkgname}/abstractrange) = %{version}
Provides:       crate(%{pkgname}/addeventlisteneroptions) = %{version}
Provides:       crate(%{pkgname}/aescbcparams) = %{version}
Provides:       crate(%{pkgname}/aesctrparams) = %{version}
Provides:       crate(%{pkgname}/aesderivedkeyparams) = %{version}
Provides:       crate(%{pkgname}/aesgcmparams) = %{version}
Provides:       crate(%{pkgname}/aeskeyalgorithm) = %{version}
Provides:       crate(%{pkgname}/aeskeygenparams) = %{version}
Provides:       crate(%{pkgname}/algorithm) = %{version}
Provides:       crate(%{pkgname}/alignsetting) = %{version}
Provides:       crate(%{pkgname}/allowedbluetoothdevice) = %{version}
Provides:       crate(%{pkgname}/allowedusbdevice) = %{version}
Provides:       crate(%{pkgname}/alphaoption) = %{version}
Provides:       crate(%{pkgname}/analyseroptions) = %{version}
Provides:       crate(%{pkgname}/angleinstancedarrays) = %{version}
Provides:       crate(%{pkgname}/animation) = %{version}
Provides:       crate(%{pkgname}/animationeffect) = %{version}
Provides:       crate(%{pkgname}/animationevent) = %{version}
Provides:       crate(%{pkgname}/animationeventinit) = %{version}
Provides:       crate(%{pkgname}/animationplaybackevent) = %{version}
Provides:       crate(%{pkgname}/animationplaybackeventinit) = %{version}
Provides:       crate(%{pkgname}/animationplaystate) = %{version}
Provides:       crate(%{pkgname}/animationpropertydetails) = %{version}
Provides:       crate(%{pkgname}/animationpropertyvaluedetails) = %{version}
Provides:       crate(%{pkgname}/animationtimeline) = %{version}
Provides:       crate(%{pkgname}/assignednodesoptions) = %{version}
Provides:       crate(%{pkgname}/attestationconveyancepreference) = %{version}
Provides:       crate(%{pkgname}/attributenamevalue) = %{version}
Provides:       crate(%{pkgname}/audiobuffer) = %{version}
Provides:       crate(%{pkgname}/audiobufferoptions) = %{version}
Provides:       crate(%{pkgname}/audiobuffersourceoptions) = %{version}
Provides:       crate(%{pkgname}/audioconfiguration) = %{version}
Provides:       crate(%{pkgname}/audiocontextlatencycategory) = %{version}
Provides:       crate(%{pkgname}/audiocontextoptions) = %{version}
Provides:       crate(%{pkgname}/audiocontextstate) = %{version}
Provides:       crate(%{pkgname}/audiodata) = %{version}
Provides:       crate(%{pkgname}/audiodatacopytooptions) = %{version}
Provides:       crate(%{pkgname}/audiodatainit) = %{version}
Provides:       crate(%{pkgname}/audiodecoder) = %{version}
Provides:       crate(%{pkgname}/audiodecoderconfig) = %{version}
Provides:       crate(%{pkgname}/audiodecoderinit) = %{version}
Provides:       crate(%{pkgname}/audiodecodersupport) = %{version}
Provides:       crate(%{pkgname}/audioencoder) = %{version}
Provides:       crate(%{pkgname}/audioencoderconfig) = %{version}
Provides:       crate(%{pkgname}/audioencoderinit) = %{version}
Provides:       crate(%{pkgname}/audioencodersupport) = %{version}
Provides:       crate(%{pkgname}/audiolistener) = %{version}
Provides:       crate(%{pkgname}/audionode) = %{version}
Provides:       crate(%{pkgname}/audionodeoptions) = %{version}
Provides:       crate(%{pkgname}/audioparam) = %{version}
Provides:       crate(%{pkgname}/audioparammap) = %{version}
Provides:       crate(%{pkgname}/audioprocessingevent) = %{version}
Provides:       crate(%{pkgname}/audiosampleformat) = %{version}
Provides:       crate(%{pkgname}/audiosinkinfo) = %{version}
Provides:       crate(%{pkgname}/audiosinkoptions) = %{version}
Provides:       crate(%{pkgname}/audiosinktype) = %{version}
Provides:       crate(%{pkgname}/audiotrack) = %{version}
Provides:       crate(%{pkgname}/audiotracklist) = %{version}
Provides:       crate(%{pkgname}/audioworklet) = %{version}
Provides:       crate(%{pkgname}/audioworkletglobalscope) = %{version}
Provides:       crate(%{pkgname}/audioworkletnodeoptions) = %{version}
Provides:       crate(%{pkgname}/audioworkletprocessor) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsclientinputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsclientinputsjson) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsclientoutputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsclientoutputsjson) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsdevicepublickeyinputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsdevicepublickeyoutputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionslargeblobinputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionslargebloboutputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsprfinputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsprfoutputs) = %{version}
Provides:       crate(%{pkgname}/authenticationextensionsprfvalues) = %{version}
Provides:       crate(%{pkgname}/authenticationresponsejson) = %{version}
Provides:       crate(%{pkgname}/authenticatorassertionresponse) = %{version}
Provides:       crate(%{pkgname}/authenticatorassertionresponsejson) = %{version}
Provides:       crate(%{pkgname}/authenticatorattachment) = %{version}
Provides:       crate(%{pkgname}/authenticatorattestationresponse) = %{version}
Provides:       crate(%{pkgname}/authenticatorattestationresponsejson) = %{version}
Provides:       crate(%{pkgname}/authenticatorresponse) = %{version}
Provides:       crate(%{pkgname}/authenticatorselectioncriteria) = %{version}
Provides:       crate(%{pkgname}/authenticatortransport) = %{version}
Provides:       crate(%{pkgname}/autocompleteinfo) = %{version}
Provides:       crate(%{pkgname}/autokeyword) = %{version}
Provides:       crate(%{pkgname}/barprop) = %{version}
Provides:       crate(%{pkgname}/baseaudiocontext) = %{version}
Provides:       crate(%{pkgname}/basecomputedkeyframe) = %{version}
Provides:       crate(%{pkgname}/basekeyframe) = %{version}
Provides:       crate(%{pkgname}/basepropertyindexedkeyframe) = %{version}
Provides:       crate(%{pkgname}/basiccardrequest) = %{version}
Provides:       crate(%{pkgname}/basiccardresponse) = %{version}
Provides:       crate(%{pkgname}/basiccardtype) = %{version}
Provides:       crate(%{pkgname}/batterymanager) = %{version}
Provides:       crate(%{pkgname}/beforeunloadevent) = %{version}
Provides:       crate(%{pkgname}/binarytype) = %{version}
Provides:       crate(%{pkgname}/biquadfilteroptions) = %{version}
Provides:       crate(%{pkgname}/biquadfiltertype) = %{version}
Provides:       crate(%{pkgname}/bitratemode) = %{version}
Provides:       crate(%{pkgname}/blob) = %{version}
Provides:       crate(%{pkgname}/blobevent) = %{version}
Provides:       crate(%{pkgname}/blobeventinit) = %{version}
Provides:       crate(%{pkgname}/blobpropertybag) = %{version}
Provides:       crate(%{pkgname}/blockparsingoptions) = %{version}
Provides:       crate(%{pkgname}/bluetooth) = %{version}
Provides:       crate(%{pkgname}/bluetoothadvertisingevent) = %{version}
Provides:       crate(%{pkgname}/bluetoothadvertisingeventinit) = %{version}
Provides:       crate(%{pkgname}/bluetoothcharacteristicproperties) = %{version}
Provides:       crate(%{pkgname}/bluetoothdatafilterinit) = %{version}
Provides:       crate(%{pkgname}/bluetoothdevice) = %{version}
Provides:       crate(%{pkgname}/bluetoothlescanfilterinit) = %{version}
Provides:       crate(%{pkgname}/bluetoothmanufacturerdatamap) = %{version}
Provides:       crate(%{pkgname}/bluetoothpermissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/bluetoothpermissionstorage) = %{version}
Provides:       crate(%{pkgname}/bluetoothremotegattcharacteristic) = %{version}
Provides:       crate(%{pkgname}/bluetoothremotegattdescriptor) = %{version}
Provides:       crate(%{pkgname}/bluetoothremotegattserver) = %{version}
Provides:       crate(%{pkgname}/bluetoothremotegattservice) = %{version}
Provides:       crate(%{pkgname}/bluetoothservicedatamap) = %{version}
Provides:       crate(%{pkgname}/bluetoothuuid) = %{version}
Provides:       crate(%{pkgname}/boxquadoptions) = %{version}
Provides:       crate(%{pkgname}/broadcastchannel) = %{version}
Provides:       crate(%{pkgname}/browserelementdownloadoptions) = %{version}
Provides:       crate(%{pkgname}/browserelementexecutescriptoptions) = %{version}
Provides:       crate(%{pkgname}/browserfeedwriter) = %{version}
Provides:       crate(%{pkgname}/browserfindcasesensitivity) = %{version}
Provides:       crate(%{pkgname}/browserfinddirection) = %{version}
Provides:       crate(%{pkgname}/bytelengthqueuingstrategy) = %{version}
Provides:       crate(%{pkgname}/cache) = %{version}
Provides:       crate(%{pkgname}/cachebatchoperation) = %{version}
Provides:       crate(%{pkgname}/cachequeryoptions) = %{version}
Provides:       crate(%{pkgname}/cachestorage) = %{version}
Provides:       crate(%{pkgname}/cachestoragenamespace) = %{version}
Provides:       crate(%{pkgname}/canvasgradient) = %{version}
Provides:       crate(%{pkgname}/canvaspattern) = %{version}
Provides:       crate(%{pkgname}/canvasrenderingcontext2d) = %{version}
Provides:       crate(%{pkgname}/canvaswindingrule) = %{version}
Provides:       crate(%{pkgname}/caretchangedreason) = %{version}
Provides:       crate(%{pkgname}/caretposition) = %{version}
Provides:       crate(%{pkgname}/caretstatechangedeventinit) = %{version}
Provides:       crate(%{pkgname}/channelcountmode) = %{version}
Provides:       crate(%{pkgname}/channelinterpretation) = %{version}
Provides:       crate(%{pkgname}/channelmergeroptions) = %{version}
Provides:       crate(%{pkgname}/channelsplitteroptions) = %{version}
Provides:       crate(%{pkgname}/checkerboardreason) = %{version}
Provides:       crate(%{pkgname}/checkerboardreport) = %{version}
Provides:       crate(%{pkgname}/checkerboardreportservice) = %{version}
Provides:       crate(%{pkgname}/chromefilepropertybag) = %{version}
Provides:       crate(%{pkgname}/client) = %{version}
Provides:       crate(%{pkgname}/clientqueryoptions) = %{version}
Provides:       crate(%{pkgname}/clientrectsandtexts) = %{version}
Provides:       crate(%{pkgname}/clients) = %{version}
Provides:       crate(%{pkgname}/clienttype) = %{version}
Provides:       crate(%{pkgname}/clipboard) = %{version}
Provides:       crate(%{pkgname}/clipboardevent) = %{version}
Provides:       crate(%{pkgname}/clipboardeventinit) = %{version}
Provides:       crate(%{pkgname}/clipboarditem) = %{version}
Provides:       crate(%{pkgname}/clipboarditemoptions) = %{version}
Provides:       crate(%{pkgname}/clipboardpermissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/clipboardunsanitizedformats) = %{version}
Provides:       crate(%{pkgname}/closeevent) = %{version}
Provides:       crate(%{pkgname}/closeeventinit) = %{version}
Provides:       crate(%{pkgname}/codecstate) = %{version}
Provides:       crate(%{pkgname}/collectedclientdata) = %{version}
Provides:       crate(%{pkgname}/colorspaceconversion) = %{version}
Provides:       crate(%{pkgname}/commandevent) = %{version}
Provides:       crate(%{pkgname}/commandeventinit) = %{version}
Provides:       crate(%{pkgname}/compositeoperation) = %{version}
Provides:       crate(%{pkgname}/compositioneventinit) = %{version}
Provides:       crate(%{pkgname}/compressionformat) = %{version}
Provides:       crate(%{pkgname}/compressionstream) = %{version}
Provides:       crate(%{pkgname}/computedeffecttiming) = %{version}
Provides:       crate(%{pkgname}/connectiontype) = %{version}
Provides:       crate(%{pkgname}/connstatusdict) = %{version}
Provides:       crate(%{pkgname}/console) = %{version}
Provides:       crate(%{pkgname}/consolecounter) = %{version}
Provides:       crate(%{pkgname}/consolecountererror) = %{version}
Provides:       crate(%{pkgname}/consoleevent) = %{version}
Provides:       crate(%{pkgname}/consoleinstance) = %{version}
Provides:       crate(%{pkgname}/consoleinstanceoptions) = %{version}
Provides:       crate(%{pkgname}/consolelevel) = %{version}
Provides:       crate(%{pkgname}/consoleloglevel) = %{version}
Provides:       crate(%{pkgname}/consoleprofileevent) = %{version}
Provides:       crate(%{pkgname}/consolestackentry) = %{version}
Provides:       crate(%{pkgname}/consoletimererror) = %{version}
Provides:       crate(%{pkgname}/consoletimerlogorend) = %{version}
Provides:       crate(%{pkgname}/consoletimerstart) = %{version}
Provides:       crate(%{pkgname}/constantsourceoptions) = %{version}
Provides:       crate(%{pkgname}/constrainbooleanparameters) = %{version}
Provides:       crate(%{pkgname}/constraindomstringparameters) = %{version}
Provides:       crate(%{pkgname}/constraindoublerange) = %{version}
Provides:       crate(%{pkgname}/constrainlongrange) = %{version}
Provides:       crate(%{pkgname}/contextattributes2d) = %{version}
Provides:       crate(%{pkgname}/convertcoordinateoptions) = %{version}
Provides:       crate(%{pkgname}/convolveroptions) = %{version}
Provides:       crate(%{pkgname}/cookiechangeevent) = %{version}
Provides:       crate(%{pkgname}/cookiechangeeventinit) = %{version}
Provides:       crate(%{pkgname}/cookieinit) = %{version}
Provides:       crate(%{pkgname}/cookielistitem) = %{version}
Provides:       crate(%{pkgname}/cookiesamesite) = %{version}
Provides:       crate(%{pkgname}/cookiestore) = %{version}
Provides:       crate(%{pkgname}/cookiestoredeleteoptions) = %{version}
Provides:       crate(%{pkgname}/cookiestoregetoptions) = %{version}
Provides:       crate(%{pkgname}/cookiestoremanager) = %{version}
Provides:       crate(%{pkgname}/coordinates) = %{version}
Provides:       crate(%{pkgname}/countqueuingstrategy) = %{version}
Provides:       crate(%{pkgname}/credential) = %{version}
Provides:       crate(%{pkgname}/credentialcreationoptions) = %{version}
Provides:       crate(%{pkgname}/credentialpropertiesoutput) = %{version}
Provides:       crate(%{pkgname}/credentialrequestoptions) = %{version}
Provides:       crate(%{pkgname}/credentialscontainer) = %{version}
Provides:       crate(%{pkgname}/crypto) = %{version}
Provides:       crate(%{pkgname}/cryptokey) = %{version}
Provides:       crate(%{pkgname}/cryptokeypair) = %{version}
Provides:       crate(%{pkgname}/css) = %{version}
Provides:       crate(%{pkgname}/cssboxtype) = %{version}
Provides:       crate(%{pkgname}/csscounterstylerule) = %{version}
Provides:       crate(%{pkgname}/cssfontfacerule) = %{version}
Provides:       crate(%{pkgname}/cssfontfeaturevaluesrule) = %{version}
Provides:       crate(%{pkgname}/cssgroupingrule) = %{version}
Provides:       crate(%{pkgname}/cssimportrule) = %{version}
Provides:       crate(%{pkgname}/csskeyframerule) = %{version}
Provides:       crate(%{pkgname}/csskeyframesrule) = %{version}
Provides:       crate(%{pkgname}/cssnamespacerule) = %{version}
Provides:       crate(%{pkgname}/csspagerule) = %{version}
Provides:       crate(%{pkgname}/csspseudoelement) = %{version}
Provides:       crate(%{pkgname}/cssrule) = %{version}
Provides:       crate(%{pkgname}/cssrulelist) = %{version}
Provides:       crate(%{pkgname}/cssstyledeclaration) = %{version}
Provides:       crate(%{pkgname}/cssstylerule) = %{version}
Provides:       crate(%{pkgname}/cssstylesheet) = %{version}
Provides:       crate(%{pkgname}/cssstylesheetparsingmode) = %{version}
Provides:       crate(%{pkgname}/cssviewtransitionrule) = %{version}
Provides:       crate(%{pkgname}/customelementregistry) = %{version}
Provides:       crate(%{pkgname}/customevent) = %{version}
Provides:       crate(%{pkgname}/customeventinit) = %{version}
Provides:       crate(%{pkgname}/datatransfer) = %{version}
Provides:       crate(%{pkgname}/datatransferitem) = %{version}
Provides:       crate(%{pkgname}/datatransferitemlist) = %{version}
Provides:       crate(%{pkgname}/datetimevalue) = %{version}
Provides:       crate(%{pkgname}/decoderdoctornotification) = %{version}
Provides:       crate(%{pkgname}/decoderdoctornotificationtype) = %{version}
Provides:       crate(%{pkgname}/decompressionstream) = %{version}
Provides:       crate(%{pkgname}/delayoptions) = %{version}
Provides:       crate(%{pkgname}/deviceacceleration) = %{version}
Provides:       crate(%{pkgname}/deviceaccelerationinit) = %{version}
Provides:       crate(%{pkgname}/devicelightevent) = %{version}
Provides:       crate(%{pkgname}/devicelighteventinit) = %{version}
Provides:       crate(%{pkgname}/devicemotionevent) = %{version}
Provides:       crate(%{pkgname}/devicemotioneventinit) = %{version}
Provides:       crate(%{pkgname}/deviceorientationevent) = %{version}
Provides:       crate(%{pkgname}/deviceorientationeventinit) = %{version}
Provides:       crate(%{pkgname}/deviceproximityevent) = %{version}
Provides:       crate(%{pkgname}/deviceproximityeventinit) = %{version}
Provides:       crate(%{pkgname}/devicerotationrate) = %{version}
Provides:       crate(%{pkgname}/devicerotationrateinit) = %{version}
Provides:       crate(%{pkgname}/dhkeyderiveparams) = %{version}
Provides:       crate(%{pkgname}/directionsetting) = %{version}
Provides:       crate(%{pkgname}/directory) = %{version}
Provides:       crate(%{pkgname}/directorypickeroptions) = %{version}
Provides:       crate(%{pkgname}/displaymediastreamconstraints) = %{version}
Provides:       crate(%{pkgname}/displaynameoptions) = %{version}
Provides:       crate(%{pkgname}/displaynameresult) = %{version}
Provides:       crate(%{pkgname}/distancemodeltype) = %{version}
Provides:       crate(%{pkgname}/dnscachedict) = %{version}
Provides:       crate(%{pkgname}/dnscacheentry) = %{version}
Provides:       crate(%{pkgname}/dnslookupdict) = %{version}
Provides:       crate(%{pkgname}/documenttimeline) = %{version}
Provides:       crate(%{pkgname}/documenttimelineoptions) = %{version}
Provides:       crate(%{pkgname}/domerror) = %{version}
Provides:       crate(%{pkgname}/domexception) = %{version}
Provides:       crate(%{pkgname}/domimplementation) = %{version}
Provides:       crate(%{pkgname}/dommatrix) = %{version}
Provides:       crate(%{pkgname}/dommatrix2dinit) = %{version}
Provides:       crate(%{pkgname}/dommatrixinit) = %{version}
Provides:       crate(%{pkgname}/dommatrixreadonly) = %{version}
Provides:       crate(%{pkgname}/domparser) = %{version}
Provides:       crate(%{pkgname}/dompoint) = %{version}
Provides:       crate(%{pkgname}/dompointinit) = %{version}
Provides:       crate(%{pkgname}/dompointreadonly) = %{version}
Provides:       crate(%{pkgname}/domquad) = %{version}
Provides:       crate(%{pkgname}/domquadinit) = %{version}
Provides:       crate(%{pkgname}/domquadjson) = %{version}
Provides:       crate(%{pkgname}/domrect) = %{version}
Provides:       crate(%{pkgname}/domrectinit) = %{version}
Provides:       crate(%{pkgname}/domrectlist) = %{version}
Provides:       crate(%{pkgname}/domrectreadonly) = %{version}
Provides:       crate(%{pkgname}/domrequest) = %{version}
Provides:       crate(%{pkgname}/domrequestreadystate) = %{version}
Provides:       crate(%{pkgname}/domstringlist) = %{version}
Provides:       crate(%{pkgname}/domstringmap) = %{version}
Provides:       crate(%{pkgname}/domtokenlist) = %{version}
Provides:       crate(%{pkgname}/domwindowresizeeventdetail) = %{version}
Provides:       crate(%{pkgname}/doublerange) = %{version}
Provides:       crate(%{pkgname}/drageventinit) = %{version}
Provides:       crate(%{pkgname}/dynamicscompressoroptions) = %{version}
Provides:       crate(%{pkgname}/ecdhkeyderiveparams) = %{version}
Provides:       crate(%{pkgname}/ecdsaparams) = %{version}
Provides:       crate(%{pkgname}/eckeyalgorithm) = %{version}
Provides:       crate(%{pkgname}/eckeygenparams) = %{version}
Provides:       crate(%{pkgname}/eckeyimportparams) = %{version}
Provides:       crate(%{pkgname}/effecttiming) = %{version}
Provides:       crate(%{pkgname}/elementcreationoptions) = %{version}
Provides:       crate(%{pkgname}/elementdefinitionoptions) = %{version}
Provides:       crate(%{pkgname}/encodedaudiochunk) = %{version}
Provides:       crate(%{pkgname}/encodedaudiochunkinit) = %{version}
Provides:       crate(%{pkgname}/encodedaudiochunkmetadata) = %{version}
Provides:       crate(%{pkgname}/encodedaudiochunktype) = %{version}
Provides:       crate(%{pkgname}/encodedvideochunk) = %{version}
Provides:       crate(%{pkgname}/encodedvideochunkinit) = %{version}
Provides:       crate(%{pkgname}/encodedvideochunkmetadata) = %{version}
Provides:       crate(%{pkgname}/encodedvideochunktype) = %{version}
Provides:       crate(%{pkgname}/endingtypes) = %{version}
Provides:       crate(%{pkgname}/errorcallback) = %{version}
Provides:       crate(%{pkgname}/errorevent) = %{version}
Provides:       crate(%{pkgname}/erroreventinit) = %{version}
Provides:       crate(%{pkgname}/event) = %{version}
Provides:       crate(%{pkgname}/eventinit) = %{version}
Provides:       crate(%{pkgname}/eventlistener) = %{version}
Provides:       crate(%{pkgname}/eventlisteneroptions) = %{version}
Provides:       crate(%{pkgname}/eventmodifierinit) = %{version}
Provides:       crate(%{pkgname}/eventsource) = %{version}
Provides:       crate(%{pkgname}/eventsourceinit) = %{version}
Provides:       crate(%{pkgname}/eventtarget) = %{version}
Provides:       crate(%{pkgname}/exception) = %{version}
Provides:       crate(%{pkgname}/extblendminmax) = %{version}
Provides:       crate(%{pkgname}/extcolorbufferfloat) = %{version}
Provides:       crate(%{pkgname}/extcolorbufferhalffloat) = %{version}
Provides:       crate(%{pkgname}/extdisjointtimerquery) = %{version}
Provides:       crate(%{pkgname}/extendablecookiechangeeventinit) = %{version}
Provides:       crate(%{pkgname}/extendableevent) = %{version}
Provides:       crate(%{pkgname}/extendableeventinit) = %{version}
Provides:       crate(%{pkgname}/extendablemessageeventinit) = %{version}
Provides:       crate(%{pkgname}/external) = %{version}
Provides:       crate(%{pkgname}/extfragdepth) = %{version}
Provides:       crate(%{pkgname}/extshadertexturelod) = %{version}
Provides:       crate(%{pkgname}/extsrgb) = %{version}
Provides:       crate(%{pkgname}/exttexturefilteranisotropic) = %{version}
Provides:       crate(%{pkgname}/exttexturenorm16) = %{version}
Provides:       crate(%{pkgname}/fakepluginmimeentry) = %{version}
Provides:       crate(%{pkgname}/fakeplugintaginit) = %{version}
Provides:       crate(%{pkgname}/fetcheventinit) = %{version}
Provides:       crate(%{pkgname}/fetchobserver) = %{version}
Provides:       crate(%{pkgname}/fetchreadablestreamreaddataarray) = %{version}
Provides:       crate(%{pkgname}/fetchreadablestreamreaddatadone) = %{version}
Provides:       crate(%{pkgname}/fetchstate) = %{version}
Provides:       crate(%{pkgname}/file) = %{version}
Provides:       crate(%{pkgname}/filecallback) = %{version}
Provides:       crate(%{pkgname}/filelist) = %{version}
Provides:       crate(%{pkgname}/filepickeraccepttype) = %{version}
Provides:       crate(%{pkgname}/filepickeroptions) = %{version}
Provides:       crate(%{pkgname}/filepropertybag) = %{version}
Provides:       crate(%{pkgname}/filereader) = %{version}
Provides:       crate(%{pkgname}/filereadersync) = %{version}
Provides:       crate(%{pkgname}/filesystem) = %{version}
Provides:       crate(%{pkgname}/filesystemcreatewritableoptions) = %{version}
Provides:       crate(%{pkgname}/filesystemdirectoryentry) = %{version}
Provides:       crate(%{pkgname}/filesystemdirectoryhandle) = %{version}
Provides:       crate(%{pkgname}/filesystemdirectoryreader) = %{version}
Provides:       crate(%{pkgname}/filesystementriescallback) = %{version}
Provides:       crate(%{pkgname}/filesystementry) = %{version}
Provides:       crate(%{pkgname}/filesystementrycallback) = %{version}
Provides:       crate(%{pkgname}/filesystemfileentry) = %{version}
Provides:       crate(%{pkgname}/filesystemfilehandle) = %{version}
Provides:       crate(%{pkgname}/filesystemflags) = %{version}
Provides:       crate(%{pkgname}/filesystemgetdirectoryoptions) = %{version}
Provides:       crate(%{pkgname}/filesystemgetfileoptions) = %{version}
Provides:       crate(%{pkgname}/filesystemhandle) = %{version}
Provides:       crate(%{pkgname}/filesystemhandlekind) = %{version}
Provides:       crate(%{pkgname}/filesystemhandlepermissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/filesystempermissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/filesystempermissionmode) = %{version}
Provides:       crate(%{pkgname}/filesystemreadwriteoptions) = %{version}
Provides:       crate(%{pkgname}/filesystemremoveoptions) = %{version}
Provides:       crate(%{pkgname}/filesystemsyncaccesshandle) = %{version}
Provides:       crate(%{pkgname}/filesystemsyncaccesshandlemode) = %{version}
Provides:       crate(%{pkgname}/filesystemsyncaccesshandleoptions) = %{version}
Provides:       crate(%{pkgname}/filesystemwritablefilestream) = %{version}
Provides:       crate(%{pkgname}/filllightmode) = %{version}
Provides:       crate(%{pkgname}/fillmode) = %{version}
Provides:       crate(%{pkgname}/flashclassification) = %{version}
Provides:       crate(%{pkgname}/flowcontroltype) = %{version}
Provides:       crate(%{pkgname}/focuseventinit) = %{version}
Provides:       crate(%{pkgname}/focusoptions) = %{version}
Provides:       crate(%{pkgname}/fontdata) = %{version}
Provides:       crate(%{pkgname}/fontface) = %{version}
Provides:       crate(%{pkgname}/fontfacedescriptors) = %{version}
Provides:       crate(%{pkgname}/fontfaceloadstatus) = %{version}
Provides:       crate(%{pkgname}/fontfaceset) = %{version}
Provides:       crate(%{pkgname}/fontfacesetiterator) = %{version}
Provides:       crate(%{pkgname}/fontfacesetiteratorresult) = %{version}
Provides:       crate(%{pkgname}/fontfacesetloadevent) = %{version}
Provides:       crate(%{pkgname}/fontfacesetloadeventinit) = %{version}
Provides:       crate(%{pkgname}/fontfacesetloadstatus) = %{version}
Provides:       crate(%{pkgname}/formdata) = %{version}
Provides:       crate(%{pkgname}/frametype) = %{version}
Provides:       crate(%{pkgname}/fuzzingfunctions) = %{version}
Provides:       crate(%{pkgname}/gainoptions) = %{version}
Provides:       crate(%{pkgname}/gamepad) = %{version}
Provides:       crate(%{pkgname}/gamepadbutton) = %{version}
Provides:       crate(%{pkgname}/gamepadeffectparameters) = %{version}
Provides:       crate(%{pkgname}/gamepadevent) = %{version}
Provides:       crate(%{pkgname}/gamepadeventinit) = %{version}
Provides:       crate(%{pkgname}/gamepadhand) = %{version}
Provides:       crate(%{pkgname}/gamepadhapticactuator) = %{version}
Provides:       crate(%{pkgname}/gamepadhapticactuatortype) = %{version}
Provides:       crate(%{pkgname}/gamepadhapticeffecttype) = %{version}
Provides:       crate(%{pkgname}/gamepadhapticsresult) = %{version}
Provides:       crate(%{pkgname}/gamepadmappingtype) = %{version}
Provides:       crate(%{pkgname}/gamepadpose) = %{version}
Provides:       crate(%{pkgname}/gamepadtouch) = %{version}
Provides:       crate(%{pkgname}/geolocation) = %{version}
Provides:       crate(%{pkgname}/geolocationcoordinates) = %{version}
Provides:       crate(%{pkgname}/geolocationposition) = %{version}
Provides:       crate(%{pkgname}/geolocationpositionerror) = %{version}
Provides:       crate(%{pkgname}/getanimationsoptions) = %{version}
Provides:       crate(%{pkgname}/getrootnodeoptions) = %{version}
Provides:       crate(%{pkgname}/getusermediarequest) = %{version}
Provides:       crate(%{pkgname}/gpu) = %{version}
Provides:       crate(%{pkgname}/gpu-buffer-usage) = %{version}
Provides:       crate(%{pkgname}/gpu-color-write) = %{version}
Provides:       crate(%{pkgname}/gpu-map-mode) = %{version}
Provides:       crate(%{pkgname}/gpu-shader-stage) = %{version}
Provides:       crate(%{pkgname}/gpu-texture-usage) = %{version}
Provides:       crate(%{pkgname}/gpuadapter) = %{version}
Provides:       crate(%{pkgname}/gpuadapterinfo) = %{version}
Provides:       crate(%{pkgname}/gpuaddressmode) = %{version}
Provides:       crate(%{pkgname}/gpuautolayoutmode) = %{version}
Provides:       crate(%{pkgname}/gpubindgroup) = %{version}
Provides:       crate(%{pkgname}/gpubindgroupdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpubindgroupentry) = %{version}
Provides:       crate(%{pkgname}/gpubindgrouplayout) = %{version}
Provides:       crate(%{pkgname}/gpubindgrouplayoutdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpubindgrouplayoutentry) = %{version}
Provides:       crate(%{pkgname}/gpublendcomponent) = %{version}
Provides:       crate(%{pkgname}/gpublendfactor) = %{version}
Provides:       crate(%{pkgname}/gpublendoperation) = %{version}
Provides:       crate(%{pkgname}/gpublendstate) = %{version}
Provides:       crate(%{pkgname}/gpubuffer) = %{version}
Provides:       crate(%{pkgname}/gpubufferbinding) = %{version}
Provides:       crate(%{pkgname}/gpubufferbindinglayout) = %{version}
Provides:       crate(%{pkgname}/gpubufferbindingtype) = %{version}
Provides:       crate(%{pkgname}/gpubufferdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpubuffermapstate) = %{version}
Provides:       crate(%{pkgname}/gpucanvasalphamode) = %{version}
Provides:       crate(%{pkgname}/gpucanvasconfiguration) = %{version}
Provides:       crate(%{pkgname}/gpucanvascontext) = %{version}
Provides:       crate(%{pkgname}/gpucanvastonemapping) = %{version}
Provides:       crate(%{pkgname}/gpucanvastonemappingmode) = %{version}
Provides:       crate(%{pkgname}/gpucolordict) = %{version}
Provides:       crate(%{pkgname}/gpucolortargetstate) = %{version}
Provides:       crate(%{pkgname}/gpucommandbuffer) = %{version}
Provides:       crate(%{pkgname}/gpucommandbufferdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpucommandencoder) = %{version}
Provides:       crate(%{pkgname}/gpucommandencoderdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpucomparefunction) = %{version}
Provides:       crate(%{pkgname}/gpucompilationinfo) = %{version}
Provides:       crate(%{pkgname}/gpucompilationmessage) = %{version}
Provides:       crate(%{pkgname}/gpucompilationmessagetype) = %{version}
Provides:       crate(%{pkgname}/gpucomputepassdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpucomputepassencoder) = %{version}
Provides:       crate(%{pkgname}/gpucomputepasstimestampwrites) = %{version}
Provides:       crate(%{pkgname}/gpucomputepipeline) = %{version}
Provides:       crate(%{pkgname}/gpucomputepipelinedescriptor) = %{version}
Provides:       crate(%{pkgname}/gpucopyexternalimagedestinfo) = %{version}
Provides:       crate(%{pkgname}/gpucopyexternalimagesourceinfo) = %{version}
Provides:       crate(%{pkgname}/gpucullmode) = %{version}
Provides:       crate(%{pkgname}/gpudepthstencilstate) = %{version}
Provides:       crate(%{pkgname}/gpudevice) = %{version}
Provides:       crate(%{pkgname}/gpudevicedescriptor) = %{version}
Provides:       crate(%{pkgname}/gpudevicelostinfo) = %{version}
Provides:       crate(%{pkgname}/gpudevicelostreason) = %{version}
Provides:       crate(%{pkgname}/gpuerror) = %{version}
Provides:       crate(%{pkgname}/gpuerrorfilter) = %{version}
Provides:       crate(%{pkgname}/gpuextent3ddict) = %{version}
Provides:       crate(%{pkgname}/gpuexternaltexture) = %{version}
Provides:       crate(%{pkgname}/gpuexternaltexturebindinglayout) = %{version}
Provides:       crate(%{pkgname}/gpuexternaltexturedescriptor) = %{version}
Provides:       crate(%{pkgname}/gpufeaturename) = %{version}
Provides:       crate(%{pkgname}/gpufiltermode) = %{version}
Provides:       crate(%{pkgname}/gpufragmentstate) = %{version}
Provides:       crate(%{pkgname}/gpufrontface) = %{version}
Provides:       crate(%{pkgname}/gpuindexformat) = %{version}
Provides:       crate(%{pkgname}/gpuinternalerror) = %{version}
Provides:       crate(%{pkgname}/gpuloadop) = %{version}
Provides:       crate(%{pkgname}/gpumipmapfiltermode) = %{version}
Provides:       crate(%{pkgname}/gpumultisamplestate) = %{version}
Provides:       crate(%{pkgname}/gpuobjectdescriptorbase) = %{version}
Provides:       crate(%{pkgname}/gpuorigin2ddict) = %{version}
Provides:       crate(%{pkgname}/gpuorigin3ddict) = %{version}
Provides:       crate(%{pkgname}/gpuoutofmemoryerror) = %{version}
Provides:       crate(%{pkgname}/gpupipelinedescriptorbase) = %{version}
Provides:       crate(%{pkgname}/gpupipelineerror) = %{version}
Provides:       crate(%{pkgname}/gpupipelineerrorinit) = %{version}
Provides:       crate(%{pkgname}/gpupipelineerrorreason) = %{version}
Provides:       crate(%{pkgname}/gpupipelinelayout) = %{version}
Provides:       crate(%{pkgname}/gpupipelinelayoutdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpupowerpreference) = %{version}
Provides:       crate(%{pkgname}/gpuprimitivestate) = %{version}
Provides:       crate(%{pkgname}/gpuprimitivetopology) = %{version}
Provides:       crate(%{pkgname}/gpuprogrammablestage) = %{version}
Provides:       crate(%{pkgname}/gpuqueryset) = %{version}
Provides:       crate(%{pkgname}/gpuquerysetdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpuquerytype) = %{version}
Provides:       crate(%{pkgname}/gpuqueue) = %{version}
Provides:       crate(%{pkgname}/gpuqueuedescriptor) = %{version}
Provides:       crate(%{pkgname}/gpurenderbundle) = %{version}
Provides:       crate(%{pkgname}/gpurenderbundledescriptor) = %{version}
Provides:       crate(%{pkgname}/gpurenderbundleencoder) = %{version}
Provides:       crate(%{pkgname}/gpurenderbundleencoderdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpurenderpasscolorattachment) = %{version}
Provides:       crate(%{pkgname}/gpurenderpassdepthstencilattachment) = %{version}
Provides:       crate(%{pkgname}/gpurenderpassdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpurenderpassencoder) = %{version}
Provides:       crate(%{pkgname}/gpurenderpasslayout) = %{version}
Provides:       crate(%{pkgname}/gpurenderpasstimestampwrites) = %{version}
Provides:       crate(%{pkgname}/gpurenderpipeline) = %{version}
Provides:       crate(%{pkgname}/gpurenderpipelinedescriptor) = %{version}
Provides:       crate(%{pkgname}/gpurequestadapteroptions) = %{version}
Provides:       crate(%{pkgname}/gpusampler) = %{version}
Provides:       crate(%{pkgname}/gpusamplerbindinglayout) = %{version}
Provides:       crate(%{pkgname}/gpusamplerbindingtype) = %{version}
Provides:       crate(%{pkgname}/gpusamplerdescriptor) = %{version}
Provides:       crate(%{pkgname}/gpushadermodule) = %{version}
Provides:       crate(%{pkgname}/gpushadermodulecompilationhint) = %{version}
Provides:       crate(%{pkgname}/gpushadermoduledescriptor) = %{version}
Provides:       crate(%{pkgname}/gpustencilfacestate) = %{version}
Provides:       crate(%{pkgname}/gpustenciloperation) = %{version}
Provides:       crate(%{pkgname}/gpustoragetextureaccess) = %{version}
Provides:       crate(%{pkgname}/gpustoragetexturebindinglayout) = %{version}
Provides:       crate(%{pkgname}/gpustoreop) = %{version}
Provides:       crate(%{pkgname}/gpusupportedfeatures) = %{version}
Provides:       crate(%{pkgname}/gpusupportedlimits) = %{version}
Provides:       crate(%{pkgname}/gputexelcopybufferinfo) = %{version}
Provides:       crate(%{pkgname}/gputexelcopybufferlayout) = %{version}
Provides:       crate(%{pkgname}/gputexelcopytextureinfo) = %{version}
Provides:       crate(%{pkgname}/gputexture) = %{version}
Provides:       crate(%{pkgname}/gputextureaspect) = %{version}
Provides:       crate(%{pkgname}/gputexturebindinglayout) = %{version}
Provides:       crate(%{pkgname}/gputexturedescriptor) = %{version}
Provides:       crate(%{pkgname}/gputexturedimension) = %{version}
Provides:       crate(%{pkgname}/gputextureformat) = %{version}
Provides:       crate(%{pkgname}/gputexturesampletype) = %{version}
Provides:       crate(%{pkgname}/gputextureview) = %{version}
Provides:       crate(%{pkgname}/gputextureviewdescriptor) = %{version}
Provides:       crate(%{pkgname}/gputextureviewdimension) = %{version}
Provides:       crate(%{pkgname}/gpuuncapturederrorevent) = %{version}
Provides:       crate(%{pkgname}/gpuuncapturederroreventinit) = %{version}
Provides:       crate(%{pkgname}/gpuvalidationerror) = %{version}
Provides:       crate(%{pkgname}/gpuvertexattribute) = %{version}
Provides:       crate(%{pkgname}/gpuvertexbufferlayout) = %{version}
Provides:       crate(%{pkgname}/gpuvertexformat) = %{version}
Provides:       crate(%{pkgname}/gpuvertexstate) = %{version}
Provides:       crate(%{pkgname}/gpuvertexstepmode) = %{version}
Provides:       crate(%{pkgname}/groupedhistoryeventinit) = %{version}
Provides:       crate(%{pkgname}/halfopeninfodict) = %{version}
Provides:       crate(%{pkgname}/hardwareacceleration) = %{version}
Provides:       crate(%{pkgname}/hashchangeevent) = %{version}
Provides:       crate(%{pkgname}/hashchangeeventinit) = %{version}
Provides:       crate(%{pkgname}/headers) = %{version}
Provides:       crate(%{pkgname}/headersguardenum) = %{version}
Provides:       crate(%{pkgname}/hid) = %{version}
Provides:       crate(%{pkgname}/hidcollectioninfo) = %{version}
Provides:       crate(%{pkgname}/hidconnectionevent) = %{version}
Provides:       crate(%{pkgname}/hidconnectioneventinit) = %{version}
Provides:       crate(%{pkgname}/hiddenplugineventinit) = %{version}
Provides:       crate(%{pkgname}/hiddevice) = %{version}
Provides:       crate(%{pkgname}/hiddevicefilter) = %{version}
Provides:       crate(%{pkgname}/hiddevicerequestoptions) = %{version}
Provides:       crate(%{pkgname}/hidinputreportevent) = %{version}
Provides:       crate(%{pkgname}/hidinputreporteventinit) = %{version}
Provides:       crate(%{pkgname}/hidreportinfo) = %{version}
Provides:       crate(%{pkgname}/hidreportitem) = %{version}
Provides:       crate(%{pkgname}/hidunitsystem) = %{version}
Provides:       crate(%{pkgname}/highlight) = %{version}
Provides:       crate(%{pkgname}/highlighthitresult) = %{version}
Provides:       crate(%{pkgname}/highlightregistry) = %{version}
Provides:       crate(%{pkgname}/highlightsfrompointoptions) = %{version}
Provides:       crate(%{pkgname}/highlighttype) = %{version}
Provides:       crate(%{pkgname}/history) = %{version}
Provides:       crate(%{pkgname}/hitregionoptions) = %{version}
Provides:       crate(%{pkgname}/hkdfparams) = %{version}
Provides:       crate(%{pkgname}/hmacderivedkeyparams) = %{version}
Provides:       crate(%{pkgname}/hmacimportparams) = %{version}
Provides:       crate(%{pkgname}/hmackeyalgorithm) = %{version}
Provides:       crate(%{pkgname}/hmackeygenparams) = %{version}
Provides:       crate(%{pkgname}/htmlallcollection) = %{version}
Provides:       crate(%{pkgname}/htmlcollection) = %{version}
Provides:       crate(%{pkgname}/htmlformcontrolscollection) = %{version}
Provides:       crate(%{pkgname}/htmloptionscollection) = %{version}
Provides:       crate(%{pkgname}/httpconndict) = %{version}
Provides:       crate(%{pkgname}/httpconnectionelement) = %{version}
Provides:       crate(%{pkgname}/httpconninfo) = %{version}
Provides:       crate(%{pkgname}/idbcursor) = %{version}
Provides:       crate(%{pkgname}/idbcursordirection) = %{version}
Provides:       crate(%{pkgname}/idbcursorwithvalue) = %{version}
Provides:       crate(%{pkgname}/idbdatabase) = %{version}
Provides:       crate(%{pkgname}/idbfactory) = %{version}
Provides:       crate(%{pkgname}/idbfilehandle) = %{version}
Provides:       crate(%{pkgname}/idbfilemetadataparameters) = %{version}
Provides:       crate(%{pkgname}/idbindex) = %{version}
Provides:       crate(%{pkgname}/idbindexparameters) = %{version}
Provides:       crate(%{pkgname}/idbkeyrange) = %{version}
Provides:       crate(%{pkgname}/idblocaleawarekeyrange) = %{version}
Provides:       crate(%{pkgname}/idbmutablefile) = %{version}
Provides:       crate(%{pkgname}/idbobjectstore) = %{version}
Provides:       crate(%{pkgname}/idbobjectstoreparameters) = %{version}
Provides:       crate(%{pkgname}/idbopendboptions) = %{version}
Provides:       crate(%{pkgname}/idbrequest) = %{version}
Provides:       crate(%{pkgname}/idbrequestreadystate) = %{version}
Provides:       crate(%{pkgname}/idbtransaction) = %{version}
Provides:       crate(%{pkgname}/idbtransactiondurability) = %{version}
Provides:       crate(%{pkgname}/idbtransactionmode) = %{version}
Provides:       crate(%{pkgname}/idbtransactionoptions) = %{version}
Provides:       crate(%{pkgname}/idbversionchangeevent) = %{version}
Provides:       crate(%{pkgname}/idbversionchangeeventinit) = %{version}
Provides:       crate(%{pkgname}/idledeadline) = %{version}
Provides:       crate(%{pkgname}/idlerequestoptions) = %{version}
Provides:       crate(%{pkgname}/iirfilteroptions) = %{version}
Provides:       crate(%{pkgname}/imagebitmap) = %{version}
Provides:       crate(%{pkgname}/imagebitmapoptions) = %{version}
Provides:       crate(%{pkgname}/imagebitmaprenderingcontext) = %{version}
Provides:       crate(%{pkgname}/imagecapture) = %{version}
Provides:       crate(%{pkgname}/imagecaptureerror) = %{version}
Provides:       crate(%{pkgname}/imagecaptureerrorevent) = %{version}
Provides:       crate(%{pkgname}/imagecaptureerroreventinit) = %{version}
Provides:       crate(%{pkgname}/imagedata) = %{version}
Provides:       crate(%{pkgname}/imagedecodeoptions) = %{version}
Provides:       crate(%{pkgname}/imagedecoder) = %{version}
Provides:       crate(%{pkgname}/imagedecoderesult) = %{version}
Provides:       crate(%{pkgname}/imagedecoderinit) = %{version}
Provides:       crate(%{pkgname}/imageencodeoptions) = %{version}
Provides:       crate(%{pkgname}/imageorientation) = %{version}
Provides:       crate(%{pkgname}/imagetrack) = %{version}
Provides:       crate(%{pkgname}/imagetracklist) = %{version}
Provides:       crate(%{pkgname}/inputdeviceinfo) = %{version}
Provides:       crate(%{pkgname}/inputeventinit) = %{version}
Provides:       crate(%{pkgname}/intersectionobserver) = %{version}
Provides:       crate(%{pkgname}/intersectionobserverentry) = %{version}
Provides:       crate(%{pkgname}/intersectionobserverentryinit) = %{version}
Provides:       crate(%{pkgname}/intersectionobserverinit) = %{version}
Provides:       crate(%{pkgname}/intlutils) = %{version}
Provides:       crate(%{pkgname}/isinputpendingoptions) = %{version}
Provides:       crate(%{pkgname}/iterablekeyandvalueresult) = %{version}
Provides:       crate(%{pkgname}/iterablekeyorvalueresult) = %{version}
Provides:       crate(%{pkgname}/iterationcompositeoperation) = %{version}
Provides:       crate(%{pkgname}/jsonwebkey) = %{version}
Provides:       crate(%{pkgname}/keyalgorithm) = %{version}
Provides:       crate(%{pkgname}/keyboardeventinit) = %{version}
Provides:       crate(%{pkgname}/keyevent) = %{version}
Provides:       crate(%{pkgname}/keyframeanimationoptions) = %{version}
Provides:       crate(%{pkgname}/keyframeeffect) = %{version}
Provides:       crate(%{pkgname}/keyframeeffectoptions) = %{version}
Provides:       crate(%{pkgname}/keyframerequestevent) = %{version}
Provides:       crate(%{pkgname}/keyidsinitdata) = %{version}
Provides:       crate(%{pkgname}/l10nelement) = %{version}
Provides:       crate(%{pkgname}/l10nvalue) = %{version}
Provides:       crate(%{pkgname}/largeblobsupport) = %{version}
Provides:       crate(%{pkgname}/latencymode) = %{version}
Provides:       crate(%{pkgname}/lifecyclecallbacks) = %{version}
Provides:       crate(%{pkgname}/linealignsetting) = %{version}
Provides:       crate(%{pkgname}/listboxobject) = %{version}
Provides:       crate(%{pkgname}/localeinfo) = %{version}
Provides:       crate(%{pkgname}/location) = %{version}
Provides:       crate(%{pkgname}/lock) = %{version}
Provides:       crate(%{pkgname}/lockinfo) = %{version}
Provides:       crate(%{pkgname}/lockmanager) = %{version}
Provides:       crate(%{pkgname}/lockmanagersnapshot) = %{version}
Provides:       crate(%{pkgname}/lockmode) = %{version}
Provides:       crate(%{pkgname}/lockoptions) = %{version}
Provides:       crate(%{pkgname}/mediacapabilities) = %{version}
Provides:       crate(%{pkgname}/mediacapabilitiesinfo) = %{version}
Provides:       crate(%{pkgname}/mediaconfiguration) = %{version}
Provides:       crate(%{pkgname}/mediadecodingconfiguration) = %{version}
Provides:       crate(%{pkgname}/mediadecodingtype) = %{version}
Provides:       crate(%{pkgname}/mediadeviceinfo) = %{version}
Provides:       crate(%{pkgname}/mediadevicekind) = %{version}
Provides:       crate(%{pkgname}/mediadevices) = %{version}
Provides:       crate(%{pkgname}/mediaelementaudiosourceoptions) = %{version}
Provides:       crate(%{pkgname}/mediaencodingconfiguration) = %{version}
Provides:       crate(%{pkgname}/mediaencodingtype) = %{version}
Provides:       crate(%{pkgname}/mediaencryptedevent) = %{version}
Provides:       crate(%{pkgname}/mediaerror) = %{version}
Provides:       crate(%{pkgname}/mediaimage) = %{version}
Provides:       crate(%{pkgname}/mediakeyerror) = %{version}
Provides:       crate(%{pkgname}/mediakeymessageevent) = %{version}
Provides:       crate(%{pkgname}/mediakeymessageeventinit) = %{version}
Provides:       crate(%{pkgname}/mediakeymessagetype) = %{version}
Provides:       crate(%{pkgname}/mediakeyneededeventinit) = %{version}
Provides:       crate(%{pkgname}/mediakeys) = %{version}
Provides:       crate(%{pkgname}/mediakeysession) = %{version}
Provides:       crate(%{pkgname}/mediakeysessiontype) = %{version}
Provides:       crate(%{pkgname}/mediakeyspolicy) = %{version}
Provides:       crate(%{pkgname}/mediakeysrequirement) = %{version}
Provides:       crate(%{pkgname}/mediakeystatus) = %{version}
Provides:       crate(%{pkgname}/mediakeystatusmap) = %{version}
Provides:       crate(%{pkgname}/mediakeysystemaccess) = %{version}
Provides:       crate(%{pkgname}/mediakeysystemconfiguration) = %{version}
Provides:       crate(%{pkgname}/mediakeysystemmediacapability) = %{version}
Provides:       crate(%{pkgname}/mediakeysystemstatus) = %{version}
Provides:       crate(%{pkgname}/medialist) = %{version}
Provides:       crate(%{pkgname}/mediametadata) = %{version}
Provides:       crate(%{pkgname}/mediametadatainit) = %{version}
Provides:       crate(%{pkgname}/mediapositionstate) = %{version}
Provides:       crate(%{pkgname}/mediaquerylist) = %{version}
Provides:       crate(%{pkgname}/mediaquerylistevent) = %{version}
Provides:       crate(%{pkgname}/mediaquerylisteventinit) = %{version}
Provides:       crate(%{pkgname}/mediarecorder) = %{version}
Provides:       crate(%{pkgname}/mediarecordererrorevent) = %{version}
Provides:       crate(%{pkgname}/mediarecordererroreventinit) = %{version}
Provides:       crate(%{pkgname}/mediarecorderoptions) = %{version}
Provides:       crate(%{pkgname}/mediasession) = %{version}
Provides:       crate(%{pkgname}/mediasessionaction) = %{version}
Provides:       crate(%{pkgname}/mediasessionactiondetails) = %{version}
Provides:       crate(%{pkgname}/mediasessionplaybackstate) = %{version}
Provides:       crate(%{pkgname}/mediasettingsrange) = %{version}
Provides:       crate(%{pkgname}/mediasource) = %{version}
Provides:       crate(%{pkgname}/mediasourceendofstreamerror) = %{version}
Provides:       crate(%{pkgname}/mediasourceenum) = %{version}
Provides:       crate(%{pkgname}/mediasourcereadystate) = %{version}
Provides:       crate(%{pkgname}/mediastream) = %{version}
Provides:       crate(%{pkgname}/mediastreamaudiosourceoptions) = %{version}
Provides:       crate(%{pkgname}/mediastreamconstraints) = %{version}
Provides:       crate(%{pkgname}/mediastreamerror) = %{version}
Provides:       crate(%{pkgname}/mediastreamevent) = %{version}
Provides:       crate(%{pkgname}/mediastreameventinit) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrack) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrackevent) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrackeventinit) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrackgeneratorinit) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrackprocessor) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrackprocessorinit) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrackstate) = %{version}
Provides:       crate(%{pkgname}/mediatrackcapabilities) = %{version}
Provides:       crate(%{pkgname}/mediatrackconstraints) = %{version}
Provides:       crate(%{pkgname}/mediatrackconstraintset) = %{version}
Provides:       crate(%{pkgname}/mediatracksettings) = %{version}
Provides:       crate(%{pkgname}/mediatracksupportedconstraints) = %{version}
Provides:       crate(%{pkgname}/memoryattribution) = %{version}
Provides:       crate(%{pkgname}/memoryattributioncontainer) = %{version}
Provides:       crate(%{pkgname}/memorybreakdownentry) = %{version}
Provides:       crate(%{pkgname}/memorymeasurement) = %{version}
Provides:       crate(%{pkgname}/messagechannel) = %{version}
Provides:       crate(%{pkgname}/messageevent) = %{version}
Provides:       crate(%{pkgname}/messageeventinit) = %{version}
Provides:       crate(%{pkgname}/messageport) = %{version}
Provides:       crate(%{pkgname}/meteringmode) = %{version}
Provides:       crate(%{pkgname}/midiaccess) = %{version}
Provides:       crate(%{pkgname}/midiconnectionevent) = %{version}
Provides:       crate(%{pkgname}/midiconnectioneventinit) = %{version}
Provides:       crate(%{pkgname}/midiinputmap) = %{version}
Provides:       crate(%{pkgname}/midimessageevent) = %{version}
Provides:       crate(%{pkgname}/midimessageeventinit) = %{version}
Provides:       crate(%{pkgname}/midioptions) = %{version}
Provides:       crate(%{pkgname}/midioutputmap) = %{version}
Provides:       crate(%{pkgname}/midiport) = %{version}
Provides:       crate(%{pkgname}/midiportconnectionstate) = %{version}
Provides:       crate(%{pkgname}/midiportdevicestate) = %{version}
Provides:       crate(%{pkgname}/midiporttype) = %{version}
Provides:       crate(%{pkgname}/mimetype) = %{version}
Provides:       crate(%{pkgname}/mimetypearray) = %{version}
Provides:       crate(%{pkgname}/mouseeventinit) = %{version}
Provides:       crate(%{pkgname}/mozdebug) = %{version}
Provides:       crate(%{pkgname}/mutationevent) = %{version}
Provides:       crate(%{pkgname}/mutationobserver) = %{version}
Provides:       crate(%{pkgname}/mutationobserverinit) = %{version}
Provides:       crate(%{pkgname}/mutationobservinginfo) = %{version}
Provides:       crate(%{pkgname}/mutationrecord) = %{version}
Provides:       crate(%{pkgname}/namednodemap) = %{version}
Provides:       crate(%{pkgname}/nativeosfilereadoptions) = %{version}
Provides:       crate(%{pkgname}/nativeosfilewriteatomicoptions) = %{version}
Provides:       crate(%{pkgname}/navigationtype) = %{version}
Provides:       crate(%{pkgname}/navigator) = %{version}
Provides:       crate(%{pkgname}/navigatorautomationinformation) = %{version}
Provides:       crate(%{pkgname}/navigatoruabrandversion) = %{version}
Provides:       crate(%{pkgname}/navigatoruadata) = %{version}
Provides:       crate(%{pkgname}/networkcommandoptions) = %{version}
Provides:       crate(%{pkgname}/networkinformation) = %{version}
Provides:       crate(%{pkgname}/networkresultoptions) = %{version}
Provides:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/nodefilter) = %{version}
Provides:       crate(%{pkgname}/nodeiterator) = %{version}
Provides:       crate(%{pkgname}/nodelist) = %{version}
Provides:       crate(%{pkgname}/notification) = %{version}
Provides:       crate(%{pkgname}/notificationaction) = %{version}
Provides:       crate(%{pkgname}/notificationdirection) = %{version}
Provides:       crate(%{pkgname}/notificationeventinit) = %{version}
Provides:       crate(%{pkgname}/notificationoptions) = %{version}
Provides:       crate(%{pkgname}/notificationpermission) = %{version}
Provides:       crate(%{pkgname}/observercallback) = %{version}
Provides:       crate(%{pkgname}/oeselementindexuint) = %{version}
Provides:       crate(%{pkgname}/oesstandardderivatives) = %{version}
Provides:       crate(%{pkgname}/oestexturefloat) = %{version}
Provides:       crate(%{pkgname}/oestexturefloatlinear) = %{version}
Provides:       crate(%{pkgname}/oestexturehalffloat) = %{version}
Provides:       crate(%{pkgname}/oestexturehalffloatlinear) = %{version}
Provides:       crate(%{pkgname}/oesvertexarrayobject) = %{version}
Provides:       crate(%{pkgname}/offlineaudiocompletionevent) = %{version}
Provides:       crate(%{pkgname}/offlineaudiocompletioneventinit) = %{version}
Provides:       crate(%{pkgname}/offlineaudiocontextoptions) = %{version}
Provides:       crate(%{pkgname}/offlineresourcelist) = %{version}
Provides:       crate(%{pkgname}/offscreencanvas) = %{version}
Provides:       crate(%{pkgname}/offscreencanvasrenderingcontext2d) = %{version}
Provides:       crate(%{pkgname}/openfilepickeroptions) = %{version}
Provides:       crate(%{pkgname}/openwindoweventdetail) = %{version}
Provides:       crate(%{pkgname}/optionaleffecttiming) = %{version}
Provides:       crate(%{pkgname}/orientationlocktype) = %{version}
Provides:       crate(%{pkgname}/orientationtype) = %{version}
Provides:       crate(%{pkgname}/oscillatoroptions) = %{version}
Provides:       crate(%{pkgname}/oscillatortype) = %{version}
Provides:       crate(%{pkgname}/oversampletype) = %{version}
Provides:       crate(%{pkgname}/ovrmultiview2) = %{version}
Provides:       crate(%{pkgname}/pagetransitionevent) = %{version}
Provides:       crate(%{pkgname}/pagetransitioneventinit) = %{version}
Provides:       crate(%{pkgname}/paintrequest) = %{version}
Provides:       crate(%{pkgname}/paintrequestlist) = %{version}
Provides:       crate(%{pkgname}/paintworkletglobalscope) = %{version}
Provides:       crate(%{pkgname}/panneroptions) = %{version}
Provides:       crate(%{pkgname}/panningmodeltype) = %{version}
Provides:       crate(%{pkgname}/paritytype) = %{version}
Provides:       crate(%{pkgname}/path2d) = %{version}
Provides:       crate(%{pkgname}/paymentaddress) = %{version}
Provides:       crate(%{pkgname}/paymentcomplete) = %{version}
Provides:       crate(%{pkgname}/paymentmethodchangeeventinit) = %{version}
Provides:       crate(%{pkgname}/paymentrequestupdateevent) = %{version}
Provides:       crate(%{pkgname}/paymentrequestupdateeventinit) = %{version}
Provides:       crate(%{pkgname}/paymentresponse) = %{version}
Provides:       crate(%{pkgname}/pbkdf2params) = %{version}
Provides:       crate(%{pkgname}/pcimpliceconnectionstate) = %{version}
Provides:       crate(%{pkgname}/pcimplicegatheringstate) = %{version}
Provides:       crate(%{pkgname}/pcimplsignalingstate) = %{version}
Provides:       crate(%{pkgname}/pcobserverstatetype) = %{version}
Provides:       crate(%{pkgname}/performance) = %{version}
Provides:       crate(%{pkgname}/performanceentry) = %{version}
Provides:       crate(%{pkgname}/performanceentryeventinit) = %{version}
Provides:       crate(%{pkgname}/performanceentryfilteroptions) = %{version}
Provides:       crate(%{pkgname}/performancemark) = %{version}
Provides:       crate(%{pkgname}/performancemarkoptions) = %{version}
Provides:       crate(%{pkgname}/performancemeasure) = %{version}
Provides:       crate(%{pkgname}/performancemeasureoptions) = %{version}
Provides:       crate(%{pkgname}/performancenavigation) = %{version}
Provides:       crate(%{pkgname}/performanceobserver) = %{version}
Provides:       crate(%{pkgname}/performanceobserverentrylist) = %{version}
Provides:       crate(%{pkgname}/performanceobserverinit) = %{version}
Provides:       crate(%{pkgname}/performanceresourcetiming) = %{version}
Provides:       crate(%{pkgname}/performanceservertiming) = %{version}
Provides:       crate(%{pkgname}/performancetiming) = %{version}
Provides:       crate(%{pkgname}/periodicwave) = %{version}
Provides:       crate(%{pkgname}/periodicwaveconstraints) = %{version}
Provides:       crate(%{pkgname}/periodicwaveoptions) = %{version}
Provides:       crate(%{pkgname}/permissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/permissionname) = %{version}
Provides:       crate(%{pkgname}/permissions) = %{version}
Provides:       crate(%{pkgname}/permissionstate) = %{version}
Provides:       crate(%{pkgname}/permissionstatus) = %{version}
Provides:       crate(%{pkgname}/photocapabilities) = %{version}
Provides:       crate(%{pkgname}/photosettings) = %{version}
Provides:       crate(%{pkgname}/pictureinpictureevent) = %{version}
Provides:       crate(%{pkgname}/pictureinpictureeventinit) = %{version}
Provides:       crate(%{pkgname}/pictureinpicturewindow) = %{version}
Provides:       crate(%{pkgname}/planelayout) = %{version}
Provides:       crate(%{pkgname}/playbackdirection) = %{version}
Provides:       crate(%{pkgname}/plugin) = %{version}
Provides:       crate(%{pkgname}/pluginarray) = %{version}
Provides:       crate(%{pkgname}/plugincrashedeventinit) = %{version}
Provides:       crate(%{pkgname}/point2d) = %{version}
Provides:       crate(%{pkgname}/pointereventinit) = %{version}
Provides:       crate(%{pkgname}/popstateevent) = %{version}
Provides:       crate(%{pkgname}/popstateeventinit) = %{version}
Provides:       crate(%{pkgname}/popupblockedevent) = %{version}
Provides:       crate(%{pkgname}/popupblockedeventinit) = %{version}
Provides:       crate(%{pkgname}/position) = %{version}
Provides:       crate(%{pkgname}/positionalignsetting) = %{version}
Provides:       crate(%{pkgname}/positionerror) = %{version}
Provides:       crate(%{pkgname}/positionoptions) = %{version}
Provides:       crate(%{pkgname}/premultiplyalpha) = %{version}
Provides:       crate(%{pkgname}/presentation) = %{version}
Provides:       crate(%{pkgname}/presentationavailability) = %{version}
Provides:       crate(%{pkgname}/presentationconnection) = %{version}
Provides:       crate(%{pkgname}/presentationconnectionavailableevent) = %{version}
Provides:       crate(%{pkgname}/presentationconnectionavailableeventinit) = %{version}
Provides:       crate(%{pkgname}/presentationconnectionbinarytype) = %{version}
Provides:       crate(%{pkgname}/presentationconnectionclosedreason) = %{version}
Provides:       crate(%{pkgname}/presentationconnectioncloseevent) = %{version}
Provides:       crate(%{pkgname}/presentationconnectioncloseeventinit) = %{version}
Provides:       crate(%{pkgname}/presentationconnectionlist) = %{version}
Provides:       crate(%{pkgname}/presentationconnectionstate) = %{version}
Provides:       crate(%{pkgname}/presentationreceiver) = %{version}
Provides:       crate(%{pkgname}/presentationrequest) = %{version}
Provides:       crate(%{pkgname}/presentationstyle) = %{version}
Provides:       crate(%{pkgname}/profiletimelinelayerrect) = %{version}
Provides:       crate(%{pkgname}/profiletimelinemarker) = %{version}
Provides:       crate(%{pkgname}/profiletimelinemessageportoperationtype) = %{version}
Provides:       crate(%{pkgname}/profiletimelinestackframe) = %{version}
Provides:       crate(%{pkgname}/profiletimelineworkeroperationtype) = %{version}
Provides:       crate(%{pkgname}/progressevent) = %{version}
Provides:       crate(%{pkgname}/progresseventinit) = %{version}
Provides:       crate(%{pkgname}/promisenativehandler) = %{version}
Provides:       crate(%{pkgname}/promiserejectionevent) = %{version}
Provides:       crate(%{pkgname}/promiserejectioneventinit) = %{version}
Provides:       crate(%{pkgname}/publickeycredential) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialcreationoptions) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialcreationoptionsjson) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialdescriptor) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialdescriptorjson) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialentity) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialhints) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialparameters) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialrequestoptions) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialrequestoptionsjson) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialrpentity) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialtype) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialuserentity) = %{version}
Provides:       crate(%{pkgname}/publickeycredentialuserentityjson) = %{version}
Provides:       crate(%{pkgname}/pushencryptionkeyname) = %{version}
Provides:       crate(%{pkgname}/pusheventinit) = %{version}
Provides:       crate(%{pkgname}/pushmanager) = %{version}
Provides:       crate(%{pkgname}/pushmessagedata) = %{version}
Provides:       crate(%{pkgname}/pushpermissionstate) = %{version}
Provides:       crate(%{pkgname}/pushsubscription) = %{version}
Provides:       crate(%{pkgname}/pushsubscriptioninit) = %{version}
Provides:       crate(%{pkgname}/pushsubscriptionjson) = %{version}
Provides:       crate(%{pkgname}/pushsubscriptionkeys) = %{version}
Provides:       crate(%{pkgname}/pushsubscriptionoptions) = %{version}
Provides:       crate(%{pkgname}/pushsubscriptionoptionsinit) = %{version}
Provides:       crate(%{pkgname}/queryoptions) = %{version}
Provides:       crate(%{pkgname}/queuingstrategy) = %{version}
Provides:       crate(%{pkgname}/queuingstrategyinit) = %{version}
Provides:       crate(%{pkgname}/radionodelist) = %{version}
Provides:       crate(%{pkgname}/range) = %{version}
Provides:       crate(%{pkgname}/rcwnperfstats) = %{version}
Provides:       crate(%{pkgname}/rcwnstatus) = %{version}
Provides:       crate(%{pkgname}/readablebytestreamcontroller) = %{version}
Provides:       crate(%{pkgname}/readablestream) = %{version}
Provides:       crate(%{pkgname}/readablestreambyobreader) = %{version}
Provides:       crate(%{pkgname}/readablestreambyobrequest) = %{version}
Provides:       crate(%{pkgname}/readablestreamdefaultcontroller) = %{version}
Provides:       crate(%{pkgname}/readablestreamdefaultreader) = %{version}
Provides:       crate(%{pkgname}/readablestreamgetreaderoptions) = %{version}
Provides:       crate(%{pkgname}/readablestreamiteratoroptions) = %{version}
Provides:       crate(%{pkgname}/readablestreamreadermode) = %{version}
Provides:       crate(%{pkgname}/readablestreamreadresult) = %{version}
Provides:       crate(%{pkgname}/readablestreamtype) = %{version}
Provides:       crate(%{pkgname}/readablewritablepair) = %{version}
Provides:       crate(%{pkgname}/recordingstate) = %{version}
Provides:       crate(%{pkgname}/redeyereduction) = %{version}
Provides:       crate(%{pkgname}/referrerpolicy) = %{version}
Provides:       crate(%{pkgname}/registeredkey) = %{version}
Provides:       crate(%{pkgname}/registerrequest) = %{version}
Provides:       crate(%{pkgname}/registerresponse) = %{version}
Provides:       crate(%{pkgname}/registrationoptions) = %{version}
Provides:       crate(%{pkgname}/registrationresponsejson) = %{version}
Provides:       crate(%{pkgname}/request) = %{version}
Provides:       crate(%{pkgname}/requestcache) = %{version}
Provides:       crate(%{pkgname}/requestcredentials) = %{version}
Provides:       crate(%{pkgname}/requestdestination) = %{version}
Provides:       crate(%{pkgname}/requestdeviceoptions) = %{version}
Provides:       crate(%{pkgname}/requestinit) = %{version}
Provides:       crate(%{pkgname}/requestmediakeysystemaccessnotification) = %{version}
Provides:       crate(%{pkgname}/requestmode) = %{version}
Provides:       crate(%{pkgname}/requestredirect) = %{version}
Provides:       crate(%{pkgname}/residentkeyrequirement) = %{version}
Provides:       crate(%{pkgname}/resizeobserver) = %{version}
Provides:       crate(%{pkgname}/resizeobserverboxoptions) = %{version}
Provides:       crate(%{pkgname}/resizeobserverentry) = %{version}
Provides:       crate(%{pkgname}/resizeobserveroptions) = %{version}
Provides:       crate(%{pkgname}/resizeobserversize) = %{version}
Provides:       crate(%{pkgname}/resizequality) = %{version}
Provides:       crate(%{pkgname}/response) = %{version}
Provides:       crate(%{pkgname}/responseinit) = %{version}
Provides:       crate(%{pkgname}/responsetype) = %{version}
Provides:       crate(%{pkgname}/rsahashedimportparams) = %{version}
Provides:       crate(%{pkgname}/rsaoaepparams) = %{version}
Provides:       crate(%{pkgname}/rsaotherprimesinfo) = %{version}
Provides:       crate(%{pkgname}/rsapssparams) = %{version}
Provides:       crate(%{pkgname}/rtcansweroptions) = %{version}
Provides:       crate(%{pkgname}/rtcbundlepolicy) = %{version}
Provides:       crate(%{pkgname}/rtccertificate) = %{version}
Provides:       crate(%{pkgname}/rtccertificateexpiration) = %{version}
Provides:       crate(%{pkgname}/rtccodecstats) = %{version}
Provides:       crate(%{pkgname}/rtcconfiguration) = %{version}
Provides:       crate(%{pkgname}/rtcdatachannel) = %{version}
Provides:       crate(%{pkgname}/rtcdatachannelevent) = %{version}
Provides:       crate(%{pkgname}/rtcdatachanneleventinit) = %{version}
Provides:       crate(%{pkgname}/rtcdatachannelinit) = %{version}
Provides:       crate(%{pkgname}/rtcdatachannelstate) = %{version}
Provides:       crate(%{pkgname}/rtcdatachanneltype) = %{version}
Provides:       crate(%{pkgname}/rtcdegradationpreference) = %{version}
Provides:       crate(%{pkgname}/rtcdtmfsender) = %{version}
Provides:       crate(%{pkgname}/rtcdtmftonechangeevent) = %{version}
Provides:       crate(%{pkgname}/rtcdtmftonechangeeventinit) = %{version}
Provides:       crate(%{pkgname}/rtcencodedaudioframe) = %{version}
Provides:       crate(%{pkgname}/rtcencodedaudioframemetadata) = %{version}
Provides:       crate(%{pkgname}/rtcencodedaudioframeoptions) = %{version}
Provides:       crate(%{pkgname}/rtcencodedvideoframe) = %{version}
Provides:       crate(%{pkgname}/rtcencodedvideoframemetadata) = %{version}
Provides:       crate(%{pkgname}/rtcencodedvideoframeoptions) = %{version}
Provides:       crate(%{pkgname}/rtcencodedvideoframetype) = %{version}
Provides:       crate(%{pkgname}/rtcfecparameters) = %{version}
Provides:       crate(%{pkgname}/rtcicecandidate) = %{version}
Provides:       crate(%{pkgname}/rtcicecandidateinit) = %{version}
Provides:       crate(%{pkgname}/rtcicecandidatepairstats) = %{version}
Provides:       crate(%{pkgname}/rtcicecandidatestats) = %{version}
Provides:       crate(%{pkgname}/rtcicecomponentstats) = %{version}
Provides:       crate(%{pkgname}/rtciceconnectionstate) = %{version}
Provides:       crate(%{pkgname}/rtcicecredentialtype) = %{version}
Provides:       crate(%{pkgname}/rtcicegatheringstate) = %{version}
Provides:       crate(%{pkgname}/rtciceserver) = %{version}
Provides:       crate(%{pkgname}/rtcicetransportpolicy) = %{version}
Provides:       crate(%{pkgname}/rtcidentityassertion) = %{version}
Provides:       crate(%{pkgname}/rtcidentityassertionresult) = %{version}
Provides:       crate(%{pkgname}/rtcidentityprovider) = %{version}
Provides:       crate(%{pkgname}/rtcidentityproviderdetails) = %{version}
Provides:       crate(%{pkgname}/rtcidentityprovideroptions) = %{version}
Provides:       crate(%{pkgname}/rtcidentityproviderregistrar) = %{version}
Provides:       crate(%{pkgname}/rtcidentityvalidationresult) = %{version}
Provides:       crate(%{pkgname}/rtcinboundrtpstreamstats) = %{version}
Provides:       crate(%{pkgname}/rtcmediastreamstats) = %{version}
Provides:       crate(%{pkgname}/rtcmediastreamtrackstats) = %{version}
Provides:       crate(%{pkgname}/rtcofferansweroptions) = %{version}
Provides:       crate(%{pkgname}/rtcofferoptions) = %{version}
Provides:       crate(%{pkgname}/rtcoutboundrtpstreamstats) = %{version}
Provides:       crate(%{pkgname}/rtcpeerconnection) = %{version}
Provides:       crate(%{pkgname}/rtcpeerconnectioniceerrorevent) = %{version}
Provides:       crate(%{pkgname}/rtcpeerconnectioniceevent) = %{version}
Provides:       crate(%{pkgname}/rtcpeerconnectioniceeventinit) = %{version}
Provides:       crate(%{pkgname}/rtcpeerconnectionstate) = %{version}
Provides:       crate(%{pkgname}/rtcprioritytype) = %{version}
Provides:       crate(%{pkgname}/rtcrtcpparameters) = %{version}
Provides:       crate(%{pkgname}/rtcrtpcapabilities) = %{version}
Provides:       crate(%{pkgname}/rtcrtpcodeccapability) = %{version}
Provides:       crate(%{pkgname}/rtcrtpcodecparameters) = %{version}
Provides:       crate(%{pkgname}/rtcrtpcontributingsource) = %{version}
Provides:       crate(%{pkgname}/rtcrtpcontributingsourcestats) = %{version}
Provides:       crate(%{pkgname}/rtcrtpencodingparameters) = %{version}
Provides:       crate(%{pkgname}/rtcrtpheaderextensioncapability) = %{version}
Provides:       crate(%{pkgname}/rtcrtpheaderextensionparameters) = %{version}
Provides:       crate(%{pkgname}/rtcrtpparameters) = %{version}
Provides:       crate(%{pkgname}/rtcrtpreceiver) = %{version}
Provides:       crate(%{pkgname}/rtcrtpscripttransform) = %{version}
Provides:       crate(%{pkgname}/rtcrtpscripttransformer) = %{version}
Provides:       crate(%{pkgname}/rtcrtpsender) = %{version}
Provides:       crate(%{pkgname}/rtcrtpsourceentry) = %{version}
Provides:       crate(%{pkgname}/rtcrtpsourceentrytype) = %{version}
Provides:       crate(%{pkgname}/rtcrtpstreamstats) = %{version}
Provides:       crate(%{pkgname}/rtcrtpsynchronizationsource) = %{version}
Provides:       crate(%{pkgname}/rtcrtptransceiver) = %{version}
Provides:       crate(%{pkgname}/rtcrtptransceiverdirection) = %{version}
Provides:       crate(%{pkgname}/rtcrtptransceiverinit) = %{version}
Provides:       crate(%{pkgname}/rtcrtxparameters) = %{version}
Provides:       crate(%{pkgname}/rtcsdptype) = %{version}
Provides:       crate(%{pkgname}/rtcsessiondescription) = %{version}
Provides:       crate(%{pkgname}/rtcsessiondescriptioninit) = %{version}
Provides:       crate(%{pkgname}/rtcsignalingstate) = %{version}
Provides:       crate(%{pkgname}/rtcstats) = %{version}
Provides:       crate(%{pkgname}/rtcstatsicecandidatepairstate) = %{version}
Provides:       crate(%{pkgname}/rtcstatsicecandidatetype) = %{version}
Provides:       crate(%{pkgname}/rtcstatsreport) = %{version}
Provides:       crate(%{pkgname}/rtcstatsreportinternal) = %{version}
Provides:       crate(%{pkgname}/rtcstatstype) = %{version}
Provides:       crate(%{pkgname}/rtctrackevent) = %{version}
Provides:       crate(%{pkgname}/rtctrackeventinit) = %{version}
Provides:       crate(%{pkgname}/rtctransformevent) = %{version}
Provides:       crate(%{pkgname}/rtctransportstats) = %{version}
Provides:       crate(%{pkgname}/savefilepickeroptions) = %{version}
Provides:       crate(%{pkgname}/scheduler) = %{version}
Provides:       crate(%{pkgname}/schedulerposttaskoptions) = %{version}
Provides:       crate(%{pkgname}/scheduling) = %{version}
Provides:       crate(%{pkgname}/screen) = %{version}
Provides:       crate(%{pkgname}/screencolorgamut) = %{version}
Provides:       crate(%{pkgname}/screendetails) = %{version}
Provides:       crate(%{pkgname}/screenluminance) = %{version}
Provides:       crate(%{pkgname}/screenorientation) = %{version}
Provides:       crate(%{pkgname}/scrollbehavior) = %{version}
Provides:       crate(%{pkgname}/scrollboxobject) = %{version}
Provides:       crate(%{pkgname}/scrollintoviewcontainer) = %{version}
Provides:       crate(%{pkgname}/scrollintoviewoptions) = %{version}
Provides:       crate(%{pkgname}/scrolllogicalposition) = %{version}
Provides:       crate(%{pkgname}/scrolloptions) = %{version}
Provides:       crate(%{pkgname}/scrollrestoration) = %{version}
Provides:       crate(%{pkgname}/scrollsetting) = %{version}
Provides:       crate(%{pkgname}/scrollstate) = %{version}
Provides:       crate(%{pkgname}/scrolltooptions) = %{version}
Provides:       crate(%{pkgname}/scrollviewchangeeventinit) = %{version}
Provides:       crate(%{pkgname}/securitypolicyviolationevent) = %{version}
Provides:       crate(%{pkgname}/securitypolicyviolationeventdisposition) = %{version}
Provides:       crate(%{pkgname}/securitypolicyviolationeventinit) = %{version}
Provides:       crate(%{pkgname}/selection) = %{version}
Provides:       crate(%{pkgname}/selectionmode) = %{version}
Provides:       crate(%{pkgname}/serial) = %{version}
Provides:       crate(%{pkgname}/serialinputsignals) = %{version}
Provides:       crate(%{pkgname}/serialoptions) = %{version}
Provides:       crate(%{pkgname}/serialoutputsignals) = %{version}
Provides:       crate(%{pkgname}/serialport) = %{version}
Provides:       crate(%{pkgname}/serialportfilter) = %{version}
Provides:       crate(%{pkgname}/serialportinfo) = %{version}
Provides:       crate(%{pkgname}/serialportrequestoptions) = %{version}
Provides:       crate(%{pkgname}/serversocketoptions) = %{version}
Provides:       crate(%{pkgname}/serviceworker) = %{version}
Provides:       crate(%{pkgname}/serviceworkercontainer) = %{version}
Provides:       crate(%{pkgname}/serviceworkerregistration) = %{version}
Provides:       crate(%{pkgname}/serviceworkerstate) = %{version}
Provides:       crate(%{pkgname}/serviceworkerupdateviacache) = %{version}
Provides:       crate(%{pkgname}/sframetransform) = %{version}
Provides:       crate(%{pkgname}/sframetransformerrorevent) = %{version}
Provides:       crate(%{pkgname}/sframetransformerroreventinit) = %{version}
Provides:       crate(%{pkgname}/sframetransformerroreventtype) = %{version}
Provides:       crate(%{pkgname}/sframetransformoptions) = %{version}
Provides:       crate(%{pkgname}/sframetransformrole) = %{version}
Provides:       crate(%{pkgname}/shadowrootinit) = %{version}
Provides:       crate(%{pkgname}/shadowrootmode) = %{version}
Provides:       crate(%{pkgname}/sharedata) = %{version}
Provides:       crate(%{pkgname}/sharedworker) = %{version}
Provides:       crate(%{pkgname}/showpopoveroptions) = %{version}
Provides:       crate(%{pkgname}/signresponse) = %{version}
Provides:       crate(%{pkgname}/socketelement) = %{version}
Provides:       crate(%{pkgname}/socketoptions) = %{version}
Provides:       crate(%{pkgname}/socketreadystate) = %{version}
Provides:       crate(%{pkgname}/socketsdict) = %{version}
Provides:       crate(%{pkgname}/sourcebuffer) = %{version}
Provides:       crate(%{pkgname}/sourcebufferappendmode) = %{version}
Provides:       crate(%{pkgname}/sourcebufferlist) = %{version}
Provides:       crate(%{pkgname}/speechgrammar) = %{version}
Provides:       crate(%{pkgname}/speechgrammarlist) = %{version}
Provides:       crate(%{pkgname}/speechrecognition) = %{version}
Provides:       crate(%{pkgname}/speechrecognitionalternative) = %{version}
Provides:       crate(%{pkgname}/speechrecognitionerror) = %{version}
Provides:       crate(%{pkgname}/speechrecognitionerrorcode) = %{version}
Provides:       crate(%{pkgname}/speechrecognitionerrorinit) = %{version}
Provides:       crate(%{pkgname}/speechrecognitionevent) = %{version}
Provides:       crate(%{pkgname}/speechrecognitioneventinit) = %{version}
Provides:       crate(%{pkgname}/speechrecognitionresult) = %{version}
Provides:       crate(%{pkgname}/speechrecognitionresultlist) = %{version}
Provides:       crate(%{pkgname}/speechsynthesis) = %{version}
Provides:       crate(%{pkgname}/speechsynthesiserrorcode) = %{version}
Provides:       crate(%{pkgname}/speechsynthesiserroreventinit) = %{version}
Provides:       crate(%{pkgname}/speechsynthesisevent) = %{version}
Provides:       crate(%{pkgname}/speechsynthesiseventinit) = %{version}
Provides:       crate(%{pkgname}/speechsynthesisutterance) = %{version}
Provides:       crate(%{pkgname}/speechsynthesisvoice) = %{version}
Provides:       crate(%{pkgname}/startviewtransitionoptions) = %{version}
Provides:       crate(%{pkgname}/staticrange) = %{version}
Provides:       crate(%{pkgname}/staticrangeinit) = %{version}
Provides:       crate(%{pkgname}/stereopanneroptions) = %{version}
Provides:       crate(%{pkgname}/storage) = %{version}
Provides:       crate(%{pkgname}/storageestimate) = %{version}
Provides:       crate(%{pkgname}/storageevent) = %{version}
Provides:       crate(%{pkgname}/storageeventinit) = %{version}
Provides:       crate(%{pkgname}/storagemanager) = %{version}
Provides:       crate(%{pkgname}/storagetype) = %{version}
Provides:       crate(%{pkgname}/streampipeoptions) = %{version}
Provides:       crate(%{pkgname}/stylerulechangeeventinit) = %{version}
Provides:       crate(%{pkgname}/stylesheet) = %{version}
Provides:       crate(%{pkgname}/stylesheetapplicablestatechangeeventinit) = %{version}
Provides:       crate(%{pkgname}/stylesheetchangeeventinit) = %{version}
Provides:       crate(%{pkgname}/stylesheetlist) = %{version}
Provides:       crate(%{pkgname}/submitevent) = %{version}
Provides:       crate(%{pkgname}/submiteventinit) = %{version}
Provides:       crate(%{pkgname}/subtlecrypto) = %{version}
Provides:       crate(%{pkgname}/supportedtype) = %{version}
Provides:       crate(%{pkgname}/svcoutputmetadata) = %{version}
Provides:       crate(%{pkgname}/svgangle) = %{version}
Provides:       crate(%{pkgname}/svganimatedangle) = %{version}
Provides:       crate(%{pkgname}/svganimatedboolean) = %{version}
Provides:       crate(%{pkgname}/svganimatedenumeration) = %{version}
Provides:       crate(%{pkgname}/svganimatedinteger) = %{version}
Provides:       crate(%{pkgname}/svganimatedlength) = %{version}
Provides:       crate(%{pkgname}/svganimatedlengthlist) = %{version}
Provides:       crate(%{pkgname}/svganimatednumber) = %{version}
Provides:       crate(%{pkgname}/svganimatednumberlist) = %{version}
Provides:       crate(%{pkgname}/svganimatedpreserveaspectratio) = %{version}
Provides:       crate(%{pkgname}/svganimatedrect) = %{version}
Provides:       crate(%{pkgname}/svganimatedstring) = %{version}
Provides:       crate(%{pkgname}/svganimatedtransformlist) = %{version}
Provides:       crate(%{pkgname}/svgboundingboxoptions) = %{version}
Provides:       crate(%{pkgname}/svglength) = %{version}
Provides:       crate(%{pkgname}/svglengthlist) = %{version}
Provides:       crate(%{pkgname}/svgmatrix) = %{version}
Provides:       crate(%{pkgname}/svgnumber) = %{version}
Provides:       crate(%{pkgname}/svgnumberlist) = %{version}
Provides:       crate(%{pkgname}/svgpathseg) = %{version}
Provides:       crate(%{pkgname}/svgpathsegarcabs) = %{version}
Provides:       crate(%{pkgname}/svgpathsegarcrel) = %{version}
Provides:       crate(%{pkgname}/svgpathsegclosepath) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetocubicabs) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetocubicrel) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetocubicsmoothabs) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetocubicsmoothrel) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetoquadraticabs) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetoquadraticrel) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetoquadraticsmoothabs) = %{version}
Provides:       crate(%{pkgname}/svgpathsegcurvetoquadraticsmoothrel) = %{version}
Provides:       crate(%{pkgname}/svgpathseglinetoabs) = %{version}
Provides:       crate(%{pkgname}/svgpathseglinetohorizontalabs) = %{version}
Provides:       crate(%{pkgname}/svgpathseglinetohorizontalrel) = %{version}
Provides:       crate(%{pkgname}/svgpathseglinetorel) = %{version}
Provides:       crate(%{pkgname}/svgpathseglinetoverticalabs) = %{version}
Provides:       crate(%{pkgname}/svgpathseglinetoverticalrel) = %{version}
Provides:       crate(%{pkgname}/svgpathseglist) = %{version}
Provides:       crate(%{pkgname}/svgpathsegmovetoabs) = %{version}
Provides:       crate(%{pkgname}/svgpathsegmovetorel) = %{version}
Provides:       crate(%{pkgname}/svgpoint) = %{version}
Provides:       crate(%{pkgname}/svgpointlist) = %{version}
Provides:       crate(%{pkgname}/svgpreserveaspectratio) = %{version}
Provides:       crate(%{pkgname}/svgrect) = %{version}
Provides:       crate(%{pkgname}/svgstringlist) = %{version}
Provides:       crate(%{pkgname}/svgtransform) = %{version}
Provides:       crate(%{pkgname}/svgtransformlist) = %{version}
Provides:       crate(%{pkgname}/svgunittypes) = %{version}
Provides:       crate(%{pkgname}/svgzoomandpan) = %{version}
Provides:       crate(%{pkgname}/taskcontroller) = %{version}
Provides:       crate(%{pkgname}/taskcontrollerinit) = %{version}
Provides:       crate(%{pkgname}/taskpriority) = %{version}
Provides:       crate(%{pkgname}/taskprioritychangeevent) = %{version}
Provides:       crate(%{pkgname}/taskprioritychangeeventinit) = %{version}
Provides:       crate(%{pkgname}/tasksignalanyinit) = %{version}
Provides:       crate(%{pkgname}/tcpreadystate) = %{version}
Provides:       crate(%{pkgname}/tcpserversocket) = %{version}
Provides:       crate(%{pkgname}/tcpserversocketevent) = %{version}
Provides:       crate(%{pkgname}/tcpserversocketeventinit) = %{version}
Provides:       crate(%{pkgname}/tcpsocket) = %{version}
Provides:       crate(%{pkgname}/tcpsocketbinarytype) = %{version}
Provides:       crate(%{pkgname}/tcpsocketerrorevent) = %{version}
Provides:       crate(%{pkgname}/tcpsocketerroreventinit) = %{version}
Provides:       crate(%{pkgname}/tcpsocketevent) = %{version}
Provides:       crate(%{pkgname}/tcpsocketeventinit) = %{version}
Provides:       crate(%{pkgname}/textdecodeoptions) = %{version}
Provides:       crate(%{pkgname}/textdecoder) = %{version}
Provides:       crate(%{pkgname}/textdecoderoptions) = %{version}
Provides:       crate(%{pkgname}/textencoder) = %{version}
Provides:       crate(%{pkgname}/textmetrics) = %{version}
Provides:       crate(%{pkgname}/texttrack) = %{version}
Provides:       crate(%{pkgname}/texttrackcue) = %{version}
Provides:       crate(%{pkgname}/texttrackcuelist) = %{version}
Provides:       crate(%{pkgname}/texttrackkind) = %{version}
Provides:       crate(%{pkgname}/texttracklist) = %{version}
Provides:       crate(%{pkgname}/texttrackmode) = %{version}
Provides:       crate(%{pkgname}/timeevent) = %{version}
Provides:       crate(%{pkgname}/timeranges) = %{version}
Provides:       crate(%{pkgname}/toggleevent) = %{version}
Provides:       crate(%{pkgname}/toggleeventinit) = %{version}
Provides:       crate(%{pkgname}/togglepopoveroptions) = %{version}
Provides:       crate(%{pkgname}/tokenbinding) = %{version}
Provides:       crate(%{pkgname}/tokenbindingstatus) = %{version}
Provides:       crate(%{pkgname}/touch) = %{version}
Provides:       crate(%{pkgname}/toucheventinit) = %{version}
Provides:       crate(%{pkgname}/touchinit) = %{version}
Provides:       crate(%{pkgname}/touchlist) = %{version}
Provides:       crate(%{pkgname}/trackevent) = %{version}
Provides:       crate(%{pkgname}/trackeventinit) = %{version}
Provides:       crate(%{pkgname}/transformer) = %{version}
Provides:       crate(%{pkgname}/transformstream) = %{version}
Provides:       crate(%{pkgname}/transformstreamdefaultcontroller) = %{version}
Provides:       crate(%{pkgname}/transitionevent) = %{version}
Provides:       crate(%{pkgname}/transitioneventinit) = %{version}
Provides:       crate(%{pkgname}/transport) = %{version}
Provides:       crate(%{pkgname}/treeboxobject) = %{version}
Provides:       crate(%{pkgname}/treecellinfo) = %{version}
Provides:       crate(%{pkgname}/treeview) = %{version}
Provides:       crate(%{pkgname}/treewalker) = %{version}
Provides:       crate(%{pkgname}/u2f) = %{version}
Provides:       crate(%{pkgname}/u2fclientdata) = %{version}
Provides:       crate(%{pkgname}/uadatavalues) = %{version}
Provides:       crate(%{pkgname}/ualowentropyjson) = %{version}
Provides:       crate(%{pkgname}/udpmessageeventinit) = %{version}
Provides:       crate(%{pkgname}/udpoptions) = %{version}
Provides:       crate(%{pkgname}/uievent) = %{version}
Provides:       crate(%{pkgname}/uieventinit) = %{version}
Provides:       crate(%{pkgname}/ulongrange) = %{version}
Provides:       crate(%{pkgname}/underlyingsink) = %{version}
Provides:       crate(%{pkgname}/underlyingsource) = %{version}
Provides:       crate(%{pkgname}/url) = %{version}
Provides:       crate(%{pkgname}/urlsearchparams) = %{version}
Provides:       crate(%{pkgname}/usb) = %{version}
Provides:       crate(%{pkgname}/usbalternateinterface) = %{version}
Provides:       crate(%{pkgname}/usbconfiguration) = %{version}
Provides:       crate(%{pkgname}/usbconnectionevent) = %{version}
Provides:       crate(%{pkgname}/usbconnectioneventinit) = %{version}
Provides:       crate(%{pkgname}/usbcontroltransferparameters) = %{version}
Provides:       crate(%{pkgname}/usbdevice) = %{version}
Provides:       crate(%{pkgname}/usbdevicefilter) = %{version}
Provides:       crate(%{pkgname}/usbdevicerequestoptions) = %{version}
Provides:       crate(%{pkgname}/usbdirection) = %{version}
Provides:       crate(%{pkgname}/usbendpoint) = %{version}
Provides:       crate(%{pkgname}/usbendpointtype) = %{version}
Provides:       crate(%{pkgname}/usbinterface) = %{version}
Provides:       crate(%{pkgname}/usbintransferresult) = %{version}
Provides:       crate(%{pkgname}/usbisochronousintransferpacket) = %{version}
Provides:       crate(%{pkgname}/usbisochronousintransferresult) = %{version}
Provides:       crate(%{pkgname}/usbisochronousouttransferpacket) = %{version}
Provides:       crate(%{pkgname}/usbisochronousouttransferresult) = %{version}
Provides:       crate(%{pkgname}/usbouttransferresult) = %{version}
Provides:       crate(%{pkgname}/usbpermissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/usbpermissionstorage) = %{version}
Provides:       crate(%{pkgname}/usbrecipient) = %{version}
Provides:       crate(%{pkgname}/usbrequesttype) = %{version}
Provides:       crate(%{pkgname}/usbtransferstatus) = %{version}
Provides:       crate(%{pkgname}/useractivation) = %{version}
Provides:       crate(%{pkgname}/userproximityevent) = %{version}
Provides:       crate(%{pkgname}/userproximityeventinit) = %{version}
Provides:       crate(%{pkgname}/userverificationrequirement) = %{version}
Provides:       crate(%{pkgname}/validitystate) = %{version}
Provides:       crate(%{pkgname}/valueevent) = %{version}
Provides:       crate(%{pkgname}/valueeventinit) = %{version}
Provides:       crate(%{pkgname}/videocolorprimaries) = %{version}
Provides:       crate(%{pkgname}/videocolorspace) = %{version}
Provides:       crate(%{pkgname}/videocolorspaceinit) = %{version}
Provides:       crate(%{pkgname}/videoconfiguration) = %{version}
Provides:       crate(%{pkgname}/videodecoder) = %{version}
Provides:       crate(%{pkgname}/videodecoderconfig) = %{version}
Provides:       crate(%{pkgname}/videodecoderinit) = %{version}
Provides:       crate(%{pkgname}/videodecodersupport) = %{version}
Provides:       crate(%{pkgname}/videoencoder) = %{version}
Provides:       crate(%{pkgname}/videoencoderbitratemode) = %{version}
Provides:       crate(%{pkgname}/videoencoderconfig) = %{version}
Provides:       crate(%{pkgname}/videoencoderencodeoptions) = %{version}
Provides:       crate(%{pkgname}/videoencoderinit) = %{version}
Provides:       crate(%{pkgname}/videoencodersupport) = %{version}
Provides:       crate(%{pkgname}/videofacingmodeenum) = %{version}
Provides:       crate(%{pkgname}/videoframe) = %{version}
Provides:       crate(%{pkgname}/videoframebufferinit) = %{version}
Provides:       crate(%{pkgname}/videoframecopytooptions) = %{version}
Provides:       crate(%{pkgname}/videoframeinit) = %{version}
Provides:       crate(%{pkgname}/videoframemetadata) = %{version}
Provides:       crate(%{pkgname}/videomatrixcoefficients) = %{version}
Provides:       crate(%{pkgname}/videopixelformat) = %{version}
Provides:       crate(%{pkgname}/videoplaybackquality) = %{version}
Provides:       crate(%{pkgname}/videotrack) = %{version}
Provides:       crate(%{pkgname}/videotracklist) = %{version}
Provides:       crate(%{pkgname}/videotransfercharacteristics) = %{version}
Provides:       crate(%{pkgname}/viewtransition) = %{version}
Provides:       crate(%{pkgname}/viewtransitiontypeset) = %{version}
Provides:       crate(%{pkgname}/visibilitystate) = %{version}
Provides:       crate(%{pkgname}/visualviewport) = %{version}
Provides:       crate(%{pkgname}/voidcallback) = %{version}
Provides:       crate(%{pkgname}/vrdisplay) = %{version}
Provides:       crate(%{pkgname}/vrdisplaycapabilities) = %{version}
Provides:       crate(%{pkgname}/vreye) = %{version}
Provides:       crate(%{pkgname}/vreyeparameters) = %{version}
Provides:       crate(%{pkgname}/vrfieldofview) = %{version}
Provides:       crate(%{pkgname}/vrframedata) = %{version}
Provides:       crate(%{pkgname}/vrlayer) = %{version}
Provides:       crate(%{pkgname}/vrmockcontroller) = %{version}
Provides:       crate(%{pkgname}/vrmockdisplay) = %{version}
Provides:       crate(%{pkgname}/vrpose) = %{version}
Provides:       crate(%{pkgname}/vrservicetest) = %{version}
Provides:       crate(%{pkgname}/vrstageparameters) = %{version}
Provides:       crate(%{pkgname}/vrsubmitframeresult) = %{version}
Provides:       crate(%{pkgname}/vttregion) = %{version}
Provides:       crate(%{pkgname}/wakelock) = %{version}
Provides:       crate(%{pkgname}/wakelocksentinel) = %{version}
Provides:       crate(%{pkgname}/wakelocktype) = %{version}
Provides:       crate(%{pkgname}/watchadvertisementsoptions) = %{version}
Provides:       crate(%{pkgname}/waveshaperoptions) = %{version}
Provides:       crate(%{pkgname}/webgl2renderingcontext) = %{version}
Provides:       crate(%{pkgname}/webglactiveinfo) = %{version}
Provides:       crate(%{pkgname}/webglbuffer) = %{version}
Provides:       crate(%{pkgname}/webglcolorbufferfloat) = %{version}
Provides:       crate(%{pkgname}/webglcompressedtextureastc) = %{version}
Provides:       crate(%{pkgname}/webglcompressedtextureatc) = %{version}
Provides:       crate(%{pkgname}/webglcompressedtextureetc) = %{version}
Provides:       crate(%{pkgname}/webglcompressedtextureetc1) = %{version}
Provides:       crate(%{pkgname}/webglcompressedtexturepvrtc) = %{version}
Provides:       crate(%{pkgname}/webglcompressedtextures3tc) = %{version}
Provides:       crate(%{pkgname}/webglcompressedtextures3tcsrgb) = %{version}
Provides:       crate(%{pkgname}/webglcontextattributes) = %{version}
Provides:       crate(%{pkgname}/webglcontextevent) = %{version}
Provides:       crate(%{pkgname}/webglcontexteventinit) = %{version}
Provides:       crate(%{pkgname}/webgldebugrendererinfo) = %{version}
Provides:       crate(%{pkgname}/webgldebugshaders) = %{version}
Provides:       crate(%{pkgname}/webgldepthtexture) = %{version}
Provides:       crate(%{pkgname}/webgldrawbuffers) = %{version}
Provides:       crate(%{pkgname}/webglframebuffer) = %{version}
Provides:       crate(%{pkgname}/webgllosecontext) = %{version}
Provides:       crate(%{pkgname}/webglmultidraw) = %{version}
Provides:       crate(%{pkgname}/webglpowerpreference) = %{version}
Provides:       crate(%{pkgname}/webglprogram) = %{version}
Provides:       crate(%{pkgname}/webglquery) = %{version}
Provides:       crate(%{pkgname}/webglrenderbuffer) = %{version}
Provides:       crate(%{pkgname}/webglrenderingcontext) = %{version}
Provides:       crate(%{pkgname}/webglsampler) = %{version}
Provides:       crate(%{pkgname}/webglshader) = %{version}
Provides:       crate(%{pkgname}/webglshaderprecisionformat) = %{version}
Provides:       crate(%{pkgname}/webglsync) = %{version}
Provides:       crate(%{pkgname}/webgltexture) = %{version}
Provides:       crate(%{pkgname}/webgltransformfeedback) = %{version}
Provides:       crate(%{pkgname}/webgluniformlocation) = %{version}
Provides:       crate(%{pkgname}/webglvertexarrayobject) = %{version}
Provides:       crate(%{pkgname}/websocket) = %{version}
Provides:       crate(%{pkgname}/websocketdict) = %{version}
Provides:       crate(%{pkgname}/websocketelement) = %{version}
Provides:       crate(%{pkgname}/webtransport) = %{version}
Provides:       crate(%{pkgname}/webtransportbidirectionalstream) = %{version}
Provides:       crate(%{pkgname}/webtransportcloseinfo) = %{version}
Provides:       crate(%{pkgname}/webtransportcongestioncontrol) = %{version}
Provides:       crate(%{pkgname}/webtransportdatagramduplexstream) = %{version}
Provides:       crate(%{pkgname}/webtransportdatagramstats) = %{version}
Provides:       crate(%{pkgname}/webtransporterror) = %{version}
Provides:       crate(%{pkgname}/webtransporterroroptions) = %{version}
Provides:       crate(%{pkgname}/webtransporterrorsource) = %{version}
Provides:       crate(%{pkgname}/webtransporthash) = %{version}
Provides:       crate(%{pkgname}/webtransportoptions) = %{version}
Provides:       crate(%{pkgname}/webtransportreceivestream) = %{version}
Provides:       crate(%{pkgname}/webtransportreceivestreamstats) = %{version}
Provides:       crate(%{pkgname}/webtransportreliabilitymode) = %{version}
Provides:       crate(%{pkgname}/webtransportsendstream) = %{version}
Provides:       crate(%{pkgname}/webtransportsendstreamoptions) = %{version}
Provides:       crate(%{pkgname}/webtransportsendstreamstats) = %{version}
Provides:       crate(%{pkgname}/webtransportstats) = %{version}
Provides:       crate(%{pkgname}/wellknowndirectory) = %{version}
Provides:       crate(%{pkgname}/wgsllanguagefeatures) = %{version}
Provides:       crate(%{pkgname}/wheeleventinit) = %{version}
Provides:       crate(%{pkgname}/widevinecdmmanifest) = %{version}
Provides:       crate(%{pkgname}/window) = %{version}
Provides:       crate(%{pkgname}/windowclient) = %{version}
Provides:       crate(%{pkgname}/worker) = %{version}
Provides:       crate(%{pkgname}/workerdebuggerglobalscope) = %{version}
Provides:       crate(%{pkgname}/workerglobalscope) = %{version}
Provides:       crate(%{pkgname}/workerlocation) = %{version}
Provides:       crate(%{pkgname}/workernavigator) = %{version}
Provides:       crate(%{pkgname}/workeroptions) = %{version}
Provides:       crate(%{pkgname}/workertype) = %{version}
Provides:       crate(%{pkgname}/worklet) = %{version}
Provides:       crate(%{pkgname}/workletglobalscope) = %{version}
Provides:       crate(%{pkgname}/workletoptions) = %{version}
Provides:       crate(%{pkgname}/writablestream) = %{version}
Provides:       crate(%{pkgname}/writablestreamdefaultcontroller) = %{version}
Provides:       crate(%{pkgname}/writablestreamdefaultwriter) = %{version}
Provides:       crate(%{pkgname}/writecommandtype) = %{version}
Provides:       crate(%{pkgname}/writeparams) = %{version}
Provides:       crate(%{pkgname}/xmlhttprequesteventtarget) = %{version}
Provides:       crate(%{pkgname}/xmlhttprequestresponsetype) = %{version}
Provides:       crate(%{pkgname}/xmlserializer) = %{version}
Provides:       crate(%{pkgname}/xpathexpression) = %{version}
Provides:       crate(%{pkgname}/xpathnsresolver) = %{version}
Provides:       crate(%{pkgname}/xpathresult) = %{version}
Provides:       crate(%{pkgname}/xreye) = %{version}
Provides:       crate(%{pkgname}/xrframe) = %{version}
Provides:       crate(%{pkgname}/xrhand) = %{version}
Provides:       crate(%{pkgname}/xrhandedness) = %{version}
Provides:       crate(%{pkgname}/xrhandjoint) = %{version}
Provides:       crate(%{pkgname}/xrinputsource) = %{version}
Provides:       crate(%{pkgname}/xrinputsourcearray) = %{version}
Provides:       crate(%{pkgname}/xrinputsourceevent) = %{version}
Provides:       crate(%{pkgname}/xrinputsourceeventinit) = %{version}
Provides:       crate(%{pkgname}/xrinputsourceschangeevent) = %{version}
Provides:       crate(%{pkgname}/xrinputsourceschangeeventinit) = %{version}
Provides:       crate(%{pkgname}/xrjointpose) = %{version}
Provides:       crate(%{pkgname}/xrlayer) = %{version}
Provides:       crate(%{pkgname}/xrpermissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/xrpose) = %{version}
Provides:       crate(%{pkgname}/xrreferencespaceevent) = %{version}
Provides:       crate(%{pkgname}/xrreferencespaceeventinit) = %{version}
Provides:       crate(%{pkgname}/xrreferencespacetype) = %{version}
Provides:       crate(%{pkgname}/xrrenderstate) = %{version}
Provides:       crate(%{pkgname}/xrrenderstateinit) = %{version}
Provides:       crate(%{pkgname}/xrrigidtransform) = %{version}
Provides:       crate(%{pkgname}/xrsession) = %{version}
Provides:       crate(%{pkgname}/xrsessionevent) = %{version}
Provides:       crate(%{pkgname}/xrsessioneventinit) = %{version}
Provides:       crate(%{pkgname}/xrsessioninit) = %{version}
Provides:       crate(%{pkgname}/xrsessionmode) = %{version}
Provides:       crate(%{pkgname}/xrsessionsupportedpermissiondescriptor) = %{version}
Provides:       crate(%{pkgname}/xrspace) = %{version}
Provides:       crate(%{pkgname}/xrsystem) = %{version}
Provides:       crate(%{pkgname}/xrtargetraymode) = %{version}
Provides:       crate(%{pkgname}/xrview) = %{version}
Provides:       crate(%{pkgname}/xrviewerpose) = %{version}
Provides:       crate(%{pkgname}/xrviewport) = %{version}
Provides:       crate(%{pkgname}/xrvisibilitystate) = %{version}
Provides:       crate(%{pkgname}/xrwebgllayerinit) = %{version}
Provides:       crate(%{pkgname}/xsltprocessor) = %{version}

%description
Source code for takopackized Rust crate "web-sys"

%package     -n %{name}+analysernode
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "AnalyserNode" and 18 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/audionode) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Provides:       crate(%{pkgname}/analysernode) = %{version}
Provides:       crate(%{pkgname}/audiodestinationnode) = %{version}
Provides:       crate(%{pkgname}/audioscheduledsourcenode) = %{version}
Provides:       crate(%{pkgname}/audioworkletnode) = %{version}
Provides:       crate(%{pkgname}/biquadfilternode) = %{version}
Provides:       crate(%{pkgname}/channelmergernode) = %{version}
Provides:       crate(%{pkgname}/channelsplitternode) = %{version}
Provides:       crate(%{pkgname}/convolvernode) = %{version}
Provides:       crate(%{pkgname}/delaynode) = %{version}
Provides:       crate(%{pkgname}/dynamicscompressornode) = %{version}
Provides:       crate(%{pkgname}/gainnode) = %{version}
Provides:       crate(%{pkgname}/iirfilternode) = %{version}
Provides:       crate(%{pkgname}/mediaelementaudiosourcenode) = %{version}
Provides:       crate(%{pkgname}/mediastreamaudiodestinationnode) = %{version}
Provides:       crate(%{pkgname}/mediastreamaudiosourcenode) = %{version}
Provides:       crate(%{pkgname}/pannernode) = %{version}
Provides:       crate(%{pkgname}/scriptprocessornode) = %{version}
Provides:       crate(%{pkgname}/stereopannernode) = %{version}
Provides:       crate(%{pkgname}/waveshapernode) = %{version}

%description -n %{name}+analysernode
This metapackage enables feature "AnalyserNode" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "AudioDestinationNode", "AudioScheduledSourceNode", "AudioWorkletNode", "BiquadFilterNode", "ChannelMergerNode", "ChannelSplitterNode", "ConvolverNode", "DelayNode", "DynamicsCompressorNode", "GainNode", "IirFilterNode", "MediaElementAudioSourceNode", "MediaStreamAudioDestinationNode", "MediaStreamAudioSourceNode", "PannerNode", "ScriptProcessorNode", "StereoPannerNode", and "WaveShaperNode" features.

%package     -n %{name}+attr
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "Attr" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/attr) = %{version}
Provides:       crate(%{pkgname}/characterdata) = %{version}
Provides:       crate(%{pkgname}/document) = %{version}
Provides:       crate(%{pkgname}/documentfragment) = %{version}
Provides:       crate(%{pkgname}/documenttype) = %{version}
Provides:       crate(%{pkgname}/element) = %{version}

%description -n %{name}+attr
This metapackage enables feature "Attr" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CharacterData", "Document", "DocumentFragment", "DocumentType", and "Element" features.

%package     -n %{name}+audiobuffersourcenode
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "AudioBufferSourceNode" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/audionode) = %{version}
Requires:       crate(%{pkgname}/audioscheduledsourcenode) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Provides:       crate(%{pkgname}/audiobuffersourcenode) = %{version}
Provides:       crate(%{pkgname}/constantsourcenode) = %{version}
Provides:       crate(%{pkgname}/oscillatornode) = %{version}

%description -n %{name}+audiobuffersourcenode
This metapackage enables feature "AudioBufferSourceNode" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ConstantSourceNode", and "OscillatorNode" features.

%package     -n %{name}+audiocontext
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "AudioContext" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/baseaudiocontext) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Provides:       crate(%{pkgname}/audiocontext) = %{version}
Provides:       crate(%{pkgname}/offlineaudiocontext) = %{version}

%description -n %{name}+audiocontext
This metapackage enables feature "AudioContext" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "OfflineAudioContext" feature.

%package     -n %{name}+audiostreamtrack
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "AudioStreamTrack" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/mediastreamtrack) = %{version}
Provides:       crate(%{pkgname}/audiostreamtrack) = %{version}
Provides:       crate(%{pkgname}/canvascapturemediastreamtrack) = %{version}
Provides:       crate(%{pkgname}/mediastreamtrackgenerator) = %{version}
Provides:       crate(%{pkgname}/videostreamtrack) = %{version}

%description -n %{name}+audiostreamtrack
This metapackage enables feature "AudioStreamTrack" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CanvasCaptureMediaStreamTrack", "MediaStreamTrackGenerator", and "VideoStreamTrack" features.

%package     -n %{name}+bluetoothpermissionresult
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "BluetoothPermissionResult" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/permissionstatus) = %{version}
Provides:       crate(%{pkgname}/bluetoothpermissionresult) = %{version}
Provides:       crate(%{pkgname}/usbpermissionresult) = %{version}
Provides:       crate(%{pkgname}/xrpermissionstatus) = %{version}

%description -n %{name}+bluetoothpermissionresult
This metapackage enables feature "BluetoothPermissionResult" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UsbPermissionResult", and "XrPermissionStatus" features.

%package     -n %{name}+canvascapturemediastream
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "CanvasCaptureMediaStream" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/mediastream) = %{version}
Provides:       crate(%{pkgname}/canvascapturemediastream) = %{version}
Provides:       crate(%{pkgname}/localmediastream) = %{version}

%description -n %{name}+canvascapturemediastream
This metapackage enables feature "CanvasCaptureMediaStream" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "LocalMediaStream" feature.

%package     -n %{name}+cdatasection
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "CdataSection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/characterdata) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/text) = %{version}
Provides:       crate(%{pkgname}/cdatasection) = %{version}

%description -n %{name}+cdatasection
This metapackage enables feature "CdataSection" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chromeworker
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "ChromeWorker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/worker) = %{version}
Provides:       crate(%{pkgname}/chromeworker) = %{version}

%description -n %{name}+chromeworker
This metapackage enables feature "ChromeWorker" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+comment
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "Comment" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/characterdata) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/comment) = %{version}
Provides:       crate(%{pkgname}/processinginstruction) = %{version}
Provides:       crate(%{pkgname}/text) = %{version}

%description -n %{name}+comment
This metapackage enables feature "Comment" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ProcessingInstruction", and "Text" features.

%package     -n %{name}+compositionevent
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "CompositionEvent" and 7 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/uievent) = %{version}
Provides:       crate(%{pkgname}/compositionevent) = %{version}
Provides:       crate(%{pkgname}/focusevent) = %{version}
Provides:       crate(%{pkgname}/gestureevent) = %{version}
Provides:       crate(%{pkgname}/inputevent) = %{version}
Provides:       crate(%{pkgname}/keyboardevent) = %{version}
Provides:       crate(%{pkgname}/mouseevent) = %{version}
Provides:       crate(%{pkgname}/scrollareaevent) = %{version}
Provides:       crate(%{pkgname}/touchevent) = %{version}

%description -n %{name}+compositionevent
This metapackage enables feature "CompositionEvent" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "FocusEvent", "GestureEvent", "InputEvent", "KeyboardEvent", "MouseEvent", "ScrollAreaEvent", and "TouchEvent" features.

%package     -n %{name}+cssanimation
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "CssAnimation" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/animation) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Provides:       crate(%{pkgname}/cssanimation) = %{version}
Provides:       crate(%{pkgname}/csstransition) = %{version}

%description -n %{name}+cssanimation
This metapackage enables feature "CssAnimation" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CssTransition" feature.

%package     -n %{name}+cssconditionrule
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "CssConditionRule"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cssgroupingrule) = %{version}
Requires:       crate(%{pkgname}/cssrule) = %{version}
Provides:       crate(%{pkgname}/cssconditionrule) = %{version}

%description -n %{name}+cssconditionrule
This metapackage enables feature "CssConditionRule" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cssmediarule
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "CssMediaRule" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cssconditionrule) = %{version}
Requires:       crate(%{pkgname}/cssgroupingrule) = %{version}
Requires:       crate(%{pkgname}/cssrule) = %{version}
Provides:       crate(%{pkgname}/cssmediarule) = %{version}
Provides:       crate(%{pkgname}/csssupportsrule) = %{version}

%description -n %{name}+cssmediarule
This metapackage enables feature "CssMediaRule" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CssSupportsRule" feature.

%package     -n %{name}+dedicatedworkerglobalscope
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "DedicatedWorkerGlobalScope" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/workerglobalscope) = %{version}
Provides:       crate(%{pkgname}/dedicatedworkerglobalscope) = %{version}
Provides:       crate(%{pkgname}/serviceworkerglobalscope) = %{version}
Provides:       crate(%{pkgname}/sharedworkerglobalscope) = %{version}

%description -n %{name}+dedicatedworkerglobalscope
This metapackage enables feature "DedicatedWorkerGlobalScope" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ServiceWorkerGlobalScope", and "SharedWorkerGlobalScope" features.

%package     -n %{name}+dragevent
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "DragEvent" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/mouseevent) = %{version}
Requires:       crate(%{pkgname}/uievent) = %{version}
Provides:       crate(%{pkgname}/dragevent) = %{version}
Provides:       crate(%{pkgname}/mousescrollevent) = %{version}
Provides:       crate(%{pkgname}/pointerevent) = %{version}
Provides:       crate(%{pkgname}/wheelevent) = %{version}

%description -n %{name}+dragevent
This metapackage enables feature "DragEvent" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MouseScrollEvent", "PointerEvent", and "WheelEvent" features.

%package     -n %{name}+extendablecookiechangeevent
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "ExtendableCookieChangeEvent" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/extendableevent) = %{version}
Provides:       crate(%{pkgname}/extendablecookiechangeevent) = %{version}
Provides:       crate(%{pkgname}/extendablemessageevent) = %{version}
Provides:       crate(%{pkgname}/fetchevent) = %{version}
Provides:       crate(%{pkgname}/notificationevent) = %{version}
Provides:       crate(%{pkgname}/pushevent) = %{version}

%description -n %{name}+extendablecookiechangeevent
This metapackage enables feature "ExtendableCookieChangeEvent" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ExtendableMessageEvent", "FetchEvent", "NotificationEvent", and "PushEvent" features.

%package     -n %{name}+htmlanchorelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "HtmlAnchorElement" and 67 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/htmlelement) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/htmlanchorelement) = %{version}
Provides:       crate(%{pkgname}/htmlareaelement) = %{version}
Provides:       crate(%{pkgname}/htmlbaseelement) = %{version}
Provides:       crate(%{pkgname}/htmlbodyelement) = %{version}
Provides:       crate(%{pkgname}/htmlbrelement) = %{version}
Provides:       crate(%{pkgname}/htmlbuttonelement) = %{version}
Provides:       crate(%{pkgname}/htmlcanvaselement) = %{version}
Provides:       crate(%{pkgname}/htmldataelement) = %{version}
Provides:       crate(%{pkgname}/htmldatalistelement) = %{version}
Provides:       crate(%{pkgname}/htmldetailselement) = %{version}
Provides:       crate(%{pkgname}/htmldialogelement) = %{version}
Provides:       crate(%{pkgname}/htmldirectoryelement) = %{version}
Provides:       crate(%{pkgname}/htmldivelement) = %{version}
Provides:       crate(%{pkgname}/htmldlistelement) = %{version}
Provides:       crate(%{pkgname}/htmlembedelement) = %{version}
Provides:       crate(%{pkgname}/htmlfieldsetelement) = %{version}
Provides:       crate(%{pkgname}/htmlfontelement) = %{version}
Provides:       crate(%{pkgname}/htmlformelement) = %{version}
Provides:       crate(%{pkgname}/htmlframeelement) = %{version}
Provides:       crate(%{pkgname}/htmlframesetelement) = %{version}
Provides:       crate(%{pkgname}/htmlheadelement) = %{version}
Provides:       crate(%{pkgname}/htmlheadingelement) = %{version}
Provides:       crate(%{pkgname}/htmlhrelement) = %{version}
Provides:       crate(%{pkgname}/htmlhtmlelement) = %{version}
Provides:       crate(%{pkgname}/htmliframeelement) = %{version}
Provides:       crate(%{pkgname}/htmlimageelement) = %{version}
Provides:       crate(%{pkgname}/htmlinputelement) = %{version}
Provides:       crate(%{pkgname}/htmllabelelement) = %{version}
Provides:       crate(%{pkgname}/htmllegendelement) = %{version}
Provides:       crate(%{pkgname}/htmllielement) = %{version}
Provides:       crate(%{pkgname}/htmllinkelement) = %{version}
Provides:       crate(%{pkgname}/htmlmapelement) = %{version}
Provides:       crate(%{pkgname}/htmlmediaelement) = %{version}
Provides:       crate(%{pkgname}/htmlmenuelement) = %{version}
Provides:       crate(%{pkgname}/htmlmenuitemelement) = %{version}
Provides:       crate(%{pkgname}/htmlmetaelement) = %{version}
Provides:       crate(%{pkgname}/htmlmeterelement) = %{version}
Provides:       crate(%{pkgname}/htmlmodelement) = %{version}
Provides:       crate(%{pkgname}/htmlobjectelement) = %{version}
Provides:       crate(%{pkgname}/htmlolistelement) = %{version}
Provides:       crate(%{pkgname}/htmloptgroupelement) = %{version}
Provides:       crate(%{pkgname}/htmloptionelement) = %{version}
Provides:       crate(%{pkgname}/htmloutputelement) = %{version}
Provides:       crate(%{pkgname}/htmlparagraphelement) = %{version}
Provides:       crate(%{pkgname}/htmlparamelement) = %{version}
Provides:       crate(%{pkgname}/htmlpictureelement) = %{version}
Provides:       crate(%{pkgname}/htmlpreelement) = %{version}
Provides:       crate(%{pkgname}/htmlprogresselement) = %{version}
Provides:       crate(%{pkgname}/htmlquoteelement) = %{version}
Provides:       crate(%{pkgname}/htmlscriptelement) = %{version}
Provides:       crate(%{pkgname}/htmlselectelement) = %{version}
Provides:       crate(%{pkgname}/htmlslotelement) = %{version}
Provides:       crate(%{pkgname}/htmlsourceelement) = %{version}
Provides:       crate(%{pkgname}/htmlspanelement) = %{version}
Provides:       crate(%{pkgname}/htmlstyleelement) = %{version}
Provides:       crate(%{pkgname}/htmltablecaptionelement) = %{version}
Provides:       crate(%{pkgname}/htmltablecellelement) = %{version}
Provides:       crate(%{pkgname}/htmltablecolelement) = %{version}
Provides:       crate(%{pkgname}/htmltableelement) = %{version}
Provides:       crate(%{pkgname}/htmltablerowelement) = %{version}
Provides:       crate(%{pkgname}/htmltablesectionelement) = %{version}
Provides:       crate(%{pkgname}/htmltemplateelement) = %{version}
Provides:       crate(%{pkgname}/htmltextareaelement) = %{version}
Provides:       crate(%{pkgname}/htmltimeelement) = %{version}
Provides:       crate(%{pkgname}/htmltitleelement) = %{version}
Provides:       crate(%{pkgname}/htmltrackelement) = %{version}
Provides:       crate(%{pkgname}/htmlulistelement) = %{version}
Provides:       crate(%{pkgname}/htmlunknownelement) = %{version}

%description -n %{name}+htmlanchorelement
This metapackage enables feature "HtmlAnchorElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "HtmlAreaElement", "HtmlBaseElement", "HtmlBodyElement", "HtmlBrElement", "HtmlButtonElement", "HtmlCanvasElement", "HtmlDListElement", "HtmlDataElement", "HtmlDataListElement", "HtmlDetailsElement", "HtmlDialogElement", "HtmlDirectoryElement", "HtmlDivElement", "HtmlEmbedElement", "HtmlFieldSetElement", "HtmlFontElement", "HtmlFormElement", "HtmlFrameElement", "HtmlFrameSetElement", "HtmlHeadElement", "HtmlHeadingElement", "HtmlHrElement", "HtmlHtmlElement", "HtmlIFrameElement", "HtmlImageElement", "HtmlInputElement", "HtmlLabelElement", "HtmlLegendElement", "HtmlLiElement", "HtmlLinkElement", "HtmlMapElement", "HtmlMediaElement", "HtmlMenuElement", "HtmlMenuItemElement", "HtmlMetaElement", "HtmlMeterElement", "HtmlModElement", "HtmlOListElement", "HtmlObjectElement", "HtmlOptGroupElement", "HtmlOptionElement", "HtmlOutputElement", "HtmlParagraphElement", "HtmlParamElement", "HtmlPictureElement", "HtmlPreElement", "HtmlProgressElement", "HtmlQuoteElement", "HtmlScriptElement", "HtmlSelectElement", "HtmlSlotElement", "HtmlSourceElement", "HtmlSpanElement", "HtmlStyleElement", "HtmlTableCaptionElement", "HtmlTableCellElement", "HtmlTableColElement", "HtmlTableElement", "HtmlTableRowElement", "HtmlTableSectionElement", "HtmlTemplateElement", "HtmlTextAreaElement", "HtmlTimeElement", "HtmlTitleElement", "HtmlTrackElement", "HtmlUListElement", and "HtmlUnknownElement" features.

%package     -n %{name}+htmlaudioelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "HtmlAudioElement" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/htmlelement) = %{version}
Requires:       crate(%{pkgname}/htmlmediaelement) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/htmlaudioelement) = %{version}
Provides:       crate(%{pkgname}/htmlvideoelement) = %{version}

%description -n %{name}+htmlaudioelement
This metapackage enables feature "HtmlAudioElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "HtmlVideoElement" feature.

%package     -n %{name}+htmldocument
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "HtmlDocument" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/document) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/htmldocument) = %{version}
Provides:       crate(%{pkgname}/xmldocument) = %{version}

%description -n %{name}+htmldocument
This metapackage enables feature "HtmlDocument" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "XmlDocument" feature.

%package     -n %{name}+htmlelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "HtmlElement" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/htmlelement) = %{version}
Provides:       crate(%{pkgname}/mathmlelement) = %{version}
Provides:       crate(%{pkgname}/svgelement) = %{version}

%description -n %{name}+htmlelement
This metapackage enables feature "HtmlElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MathMlElement", and "SvgElement" features.

%package     -n %{name}+idbfilerequest
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "IdbFileRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/domrequest) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Provides:       crate(%{pkgname}/idbfilerequest) = %{version}

%description -n %{name}+idbfilerequest
This metapackage enables feature "IdbFileRequest" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+idbopendbrequest
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "IdbOpenDbRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/idbrequest) = %{version}
Provides:       crate(%{pkgname}/idbopendbrequest) = %{version}

%description -n %{name}+idbopendbrequest
This metapackage enables feature "IdbOpenDbRequest" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+midiinput
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "MidiInput" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/midiport) = %{version}
Provides:       crate(%{pkgname}/midiinput) = %{version}
Provides:       crate(%{pkgname}/midioutput) = %{version}

%description -n %{name}+midiinput
This metapackage enables feature "MidiInput" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MidiOutput" feature.

%package     -n %{name}+paymentmethodchangeevent
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "PaymentMethodChangeEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/paymentrequestupdateevent) = %{version}
Provides:       crate(%{pkgname}/paymentmethodchangeevent) = %{version}

%description -n %{name}+paymentmethodchangeevent
This metapackage enables feature "PaymentMethodChangeEvent" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+performancenavigationtiming
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "PerformanceNavigationTiming"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/performanceentry) = %{version}
Requires:       crate(%{pkgname}/performanceresourcetiming) = %{version}
Provides:       crate(%{pkgname}/performancenavigationtiming) = %{version}

%description -n %{name}+performancenavigationtiming
This metapackage enables feature "PerformanceNavigationTiming" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+screendetailed
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "ScreenDetailed"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/screen) = %{version}
Provides:       crate(%{pkgname}/screendetailed) = %{version}

%description -n %{name}+screendetailed
This metapackage enables feature "ScreenDetailed" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shadowroot
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "ShadowRoot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/documentfragment) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Provides:       crate(%{pkgname}/shadowroot) = %{version}

%description -n %{name}+shadowroot
This metapackage enables feature "ShadowRoot" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+speechsynthesiserrorevent
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SpeechSynthesisErrorEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/speechsynthesisevent) = %{version}
Provides:       crate(%{pkgname}/speechsynthesiserrorevent) = %{version}

%description -n %{name}+speechsynthesiserrorevent
This metapackage enables feature "SpeechSynthesisErrorEvent" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+svganimateelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgAnimateElement" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svganimationelement) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Provides:       crate(%{pkgname}/svganimateelement) = %{version}
Provides:       crate(%{pkgname}/svganimatemotionelement) = %{version}
Provides:       crate(%{pkgname}/svganimatetransformelement) = %{version}
Provides:       crate(%{pkgname}/svgsetelement) = %{version}

%description -n %{name}+svganimateelement
This metapackage enables feature "SvgAnimateElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgAnimateMotionElement", "SvgAnimateTransformElement", and "SvgSetElement" features.

%package     -n %{name}+svganimationelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgAnimationElement" and 38 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Provides:       crate(%{pkgname}/svganimationelement) = %{version}
Provides:       crate(%{pkgname}/svgclippathelement) = %{version}
Provides:       crate(%{pkgname}/svgcomponenttransferfunctionelement) = %{version}
Provides:       crate(%{pkgname}/svgdescelement) = %{version}
Provides:       crate(%{pkgname}/svgfeblendelement) = %{version}
Provides:       crate(%{pkgname}/svgfecolormatrixelement) = %{version}
Provides:       crate(%{pkgname}/svgfecomponenttransferelement) = %{version}
Provides:       crate(%{pkgname}/svgfecompositeelement) = %{version}
Provides:       crate(%{pkgname}/svgfeconvolvematrixelement) = %{version}
Provides:       crate(%{pkgname}/svgfediffuselightingelement) = %{version}
Provides:       crate(%{pkgname}/svgfedisplacementmapelement) = %{version}
Provides:       crate(%{pkgname}/svgfedistantlightelement) = %{version}
Provides:       crate(%{pkgname}/svgfedropshadowelement) = %{version}
Provides:       crate(%{pkgname}/svgfefloodelement) = %{version}
Provides:       crate(%{pkgname}/svgfegaussianblurelement) = %{version}
Provides:       crate(%{pkgname}/svgfeimageelement) = %{version}
Provides:       crate(%{pkgname}/svgfemergeelement) = %{version}
Provides:       crate(%{pkgname}/svgfemergenodeelement) = %{version}
Provides:       crate(%{pkgname}/svgfemorphologyelement) = %{version}
Provides:       crate(%{pkgname}/svgfeoffsetelement) = %{version}
Provides:       crate(%{pkgname}/svgfepointlightelement) = %{version}
Provides:       crate(%{pkgname}/svgfespecularlightingelement) = %{version}
Provides:       crate(%{pkgname}/svgfespotlightelement) = %{version}
Provides:       crate(%{pkgname}/svgfetileelement) = %{version}
Provides:       crate(%{pkgname}/svgfeturbulenceelement) = %{version}
Provides:       crate(%{pkgname}/svgfilterelement) = %{version}
Provides:       crate(%{pkgname}/svggradientelement) = %{version}
Provides:       crate(%{pkgname}/svggraphicselement) = %{version}
Provides:       crate(%{pkgname}/svgmarkerelement) = %{version}
Provides:       crate(%{pkgname}/svgmaskelement) = %{version}
Provides:       crate(%{pkgname}/svgmetadataelement) = %{version}
Provides:       crate(%{pkgname}/svgmpathelement) = %{version}
Provides:       crate(%{pkgname}/svgpatternelement) = %{version}
Provides:       crate(%{pkgname}/svgscriptelement) = %{version}
Provides:       crate(%{pkgname}/svgstopelement) = %{version}
Provides:       crate(%{pkgname}/svgstyleelement) = %{version}
Provides:       crate(%{pkgname}/svgsymbolelement) = %{version}
Provides:       crate(%{pkgname}/svgtitleelement) = %{version}
Provides:       crate(%{pkgname}/svgviewelement) = %{version}

%description -n %{name}+svganimationelement
This metapackage enables feature "SvgAnimationElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgClipPathElement", "SvgComponentTransferFunctionElement", "SvgDescElement", "SvgFilterElement", "SvgGradientElement", "SvgGraphicsElement", "SvgMarkerElement", "SvgMaskElement", "SvgMetadataElement", "SvgPatternElement", "SvgScriptElement", "SvgStopElement", "SvgStyleElement", "SvgSymbolElement", "SvgTitleElement", "SvgViewElement", "SvgfeBlendElement", "SvgfeColorMatrixElement", "SvgfeComponentTransferElement", "SvgfeCompositeElement", "SvgfeConvolveMatrixElement", "SvgfeDiffuseLightingElement", "SvgfeDisplacementMapElement", "SvgfeDistantLightElement", "SvgfeDropShadowElement", "SvgfeFloodElement", "SvgfeGaussianBlurElement", "SvgfeImageElement", "SvgfeMergeElement", "SvgfeMergeNodeElement", "SvgfeMorphologyElement", "SvgfeOffsetElement", "SvgfePointLightElement", "SvgfeSpecularLightingElement", "SvgfeSpotLightElement", "SvgfeTileElement", "SvgfeTurbulenceElement", and "SvgmPathElement" features.

%package     -n %{name}+svgcircleelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgCircleElement" and 6 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Requires:       crate(%{pkgname}/svggeometryelement) = %{version}
Requires:       crate(%{pkgname}/svggraphicselement) = %{version}
Provides:       crate(%{pkgname}/svgcircleelement) = %{version}
Provides:       crate(%{pkgname}/svgellipseelement) = %{version}
Provides:       crate(%{pkgname}/svglineelement) = %{version}
Provides:       crate(%{pkgname}/svgpathelement) = %{version}
Provides:       crate(%{pkgname}/svgpolygonelement) = %{version}
Provides:       crate(%{pkgname}/svgpolylineelement) = %{version}
Provides:       crate(%{pkgname}/svgrectelement) = %{version}

%description -n %{name}+svgcircleelement
This metapackage enables feature "SvgCircleElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgEllipseElement", "SvgLineElement", "SvgPathElement", "SvgPolygonElement", "SvgPolylineElement", and "SvgRectElement" features.

%package     -n %{name}+svgdefselement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgDefsElement" and 9 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Requires:       crate(%{pkgname}/svggraphicselement) = %{version}
Provides:       crate(%{pkgname}/svgaelement) = %{version}
Provides:       crate(%{pkgname}/svgdefselement) = %{version}
Provides:       crate(%{pkgname}/svgforeignobjectelement) = %{version}
Provides:       crate(%{pkgname}/svggelement) = %{version}
Provides:       crate(%{pkgname}/svggeometryelement) = %{version}
Provides:       crate(%{pkgname}/svgimageelement) = %{version}
Provides:       crate(%{pkgname}/svgsvgelement) = %{version}
Provides:       crate(%{pkgname}/svgswitchelement) = %{version}
Provides:       crate(%{pkgname}/svgtextcontentelement) = %{version}
Provides:       crate(%{pkgname}/svguseelement) = %{version}

%description -n %{name}+svgdefselement
This metapackage enables feature "SvgDefsElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgForeignObjectElement", "SvgGeometryElement", "SvgImageElement", "SvgSwitchElement", "SvgTextContentElement", "SvgUseElement", "SvgaElement", "SvggElement", and "SvgsvgElement" features.

%package     -n %{name}+svglineargradientelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgLinearGradientElement" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Requires:       crate(%{pkgname}/svggradientelement) = %{version}
Provides:       crate(%{pkgname}/svglineargradientelement) = %{version}
Provides:       crate(%{pkgname}/svgradialgradientelement) = %{version}

%description -n %{name}+svglineargradientelement
This metapackage enables feature "SvgLinearGradientElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgRadialGradientElement" feature.

%package     -n %{name}+svgtextelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgTextElement" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Requires:       crate(%{pkgname}/svggraphicselement) = %{version}
Requires:       crate(%{pkgname}/svgtextcontentelement) = %{version}
Requires:       crate(%{pkgname}/svgtextpositioningelement) = %{version}
Provides:       crate(%{pkgname}/svgtextelement) = %{version}
Provides:       crate(%{pkgname}/svgtspanelement) = %{version}

%description -n %{name}+svgtextelement
This metapackage enables feature "SvgTextElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgtSpanElement" feature.

%package     -n %{name}+svgtextpathelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgTextPathElement" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Requires:       crate(%{pkgname}/svggraphicselement) = %{version}
Requires:       crate(%{pkgname}/svgtextcontentelement) = %{version}
Provides:       crate(%{pkgname}/svgtextpathelement) = %{version}
Provides:       crate(%{pkgname}/svgtextpositioningelement) = %{version}

%description -n %{name}+svgtextpathelement
This metapackage enables feature "SvgTextPathElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgTextPositioningElement" feature.

%package     -n %{name}+svgfefuncaelement
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "SvgfeFuncAElement" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/element) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/node) = %{version}
Requires:       crate(%{pkgname}/svgcomponenttransferfunctionelement) = %{version}
Requires:       crate(%{pkgname}/svgelement) = %{version}
Provides:       crate(%{pkgname}/svgfefuncaelement) = %{version}
Provides:       crate(%{pkgname}/svgfefuncbelement) = %{version}
Provides:       crate(%{pkgname}/svgfefuncgelement) = %{version}
Provides:       crate(%{pkgname}/svgfefuncrelement) = %{version}

%description -n %{name}+svgfefuncaelement
This metapackage enables feature "SvgfeFuncAElement" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "SvgfeFuncBElement", "SvgfeFuncGElement", and "SvgfeFuncRElement" features.

%package     -n %{name}+tasksignal
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "TaskSignal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abortsignal) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Provides:       crate(%{pkgname}/tasksignal) = %{version}

%description -n %{name}+tasksignal
This metapackage enables feature "TaskSignal" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vttcue
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "VttCue"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/texttrackcue) = %{version}
Provides:       crate(%{pkgname}/vttcue) = %{version}

%description -n %{name}+vttcue
This metapackage enables feature "VttCue" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webkitcssmatrix
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "WebKitCssMatrix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dommatrix) = %{version}
Requires:       crate(%{pkgname}/dommatrixreadonly) = %{version}
Provides:       crate(%{pkgname}/webkitcssmatrix) = %{version}

%description -n %{name}+webkitcssmatrix
This metapackage enables feature "WebKitCssMatrix" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xmlhttprequest
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "XmlHttpRequest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/xmlhttprequesteventtarget) = %{version}
Provides:       crate(%{pkgname}/xmlhttprequest) = %{version}
Provides:       crate(%{pkgname}/xmlhttprequestupload) = %{version}

%description -n %{name}+xmlhttprequest
This metapackage enables feature "XmlHttpRequest" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "XmlHttpRequestUpload" feature.

%package     -n %{name}+xrboundedreferencespace
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "XrBoundedReferenceSpace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/xrreferencespace) = %{version}
Requires:       crate(%{pkgname}/xrspace) = %{version}
Provides:       crate(%{pkgname}/xrboundedreferencespace) = %{version}

%description -n %{name}+xrboundedreferencespace
This metapackage enables feature "XrBoundedReferenceSpace" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xrjointspace
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "XrJointSpace" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/xrspace) = %{version}
Provides:       crate(%{pkgname}/xrjointspace) = %{version}
Provides:       crate(%{pkgname}/xrreferencespace) = %{version}

%description -n %{name}+xrjointspace
This metapackage enables feature "XrJointSpace" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "XrReferenceSpace" feature.

%package     -n %{name}+xrwebgllayer
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "XrWebGlLayer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eventtarget) = %{version}
Requires:       crate(%{pkgname}/xrlayer) = %{version}
Provides:       crate(%{pkgname}/xrwebgllayer) = %{version}

%description -n %{name}+xrwebgllayer
This metapackage enables feature "XrWebGlLayer" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings for all Web APIs, a procedurally generated crate from WebIDL - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/std) >= 0.3.98
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.121
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust web-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
