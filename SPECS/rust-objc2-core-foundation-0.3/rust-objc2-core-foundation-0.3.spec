# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-foundation
%global full_version 0.3.2
%global pkgname objc2-core-foundation-0.3

Name:           rust-objc2-core-foundation-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-foundation"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:2a180dd8642fa45cdb7dd721cd4c11b1cadd4929ce112ebd8b9f5803cc79d536
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cfarray) = %{version}
Provides:       crate(%{pkgname}/cfattributedstring) = %{version}
Provides:       crate(%{pkgname}/cfavailability) = %{version}
Provides:       crate(%{pkgname}/cfbag) = %{version}
Provides:       crate(%{pkgname}/cfbase) = %{version}
Provides:       crate(%{pkgname}/cfbinaryheap) = %{version}
Provides:       crate(%{pkgname}/cfbitvector) = %{version}
Provides:       crate(%{pkgname}/cfbundle) = %{version}
Provides:       crate(%{pkgname}/cfbyteorder) = %{version}
Provides:       crate(%{pkgname}/cfcgtypes) = %{version}
Provides:       crate(%{pkgname}/cfcharacterset) = %{version}
Provides:       crate(%{pkgname}/cfdictionary) = %{version}
Provides:       crate(%{pkgname}/cferror) = %{version}
Provides:       crate(%{pkgname}/cffiledescriptor) = %{version}
Provides:       crate(%{pkgname}/cflocale) = %{version}
Provides:       crate(%{pkgname}/cfmachport) = %{version}
Provides:       crate(%{pkgname}/cfmessageport) = %{version}
Provides:       crate(%{pkgname}/cfnotificationcenter) = %{version}
Provides:       crate(%{pkgname}/cfnumber) = %{version}
Provides:       crate(%{pkgname}/cfplugin) = %{version}
Provides:       crate(%{pkgname}/cfplugincom) = %{version}
Provides:       crate(%{pkgname}/cfpreferences) = %{version}
Provides:       crate(%{pkgname}/cfset) = %{version}
Provides:       crate(%{pkgname}/cfstringencodingext) = %{version}
Provides:       crate(%{pkgname}/cftimezone) = %{version}
Provides:       crate(%{pkgname}/cftree) = %{version}
Provides:       crate(%{pkgname}/cfurlaccess) = %{version}
Provides:       crate(%{pkgname}/cfusernotification) = %{version}
Provides:       crate(%{pkgname}/cfutilities) = %{version}
Provides:       crate(%{pkgname}/cfuuid) = %{version}
Provides:       crate(%{pkgname}/cfxmlnode) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-coerce-pointee) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-core-foundation"

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreFoundation framework - feature "bitflags" and 15 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/cfcalendar) = %{version}
Provides:       crate(%{pkgname}/cfdata) = %{version}
Provides:       crate(%{pkgname}/cfdate) = %{version}
Provides:       crate(%{pkgname}/cfdateformatter) = %{version}
Provides:       crate(%{pkgname}/cffilesecurity) = %{version}
Provides:       crate(%{pkgname}/cfnumberformatter) = %{version}
Provides:       crate(%{pkgname}/cfpropertylist) = %{version}
Provides:       crate(%{pkgname}/cfrunloop) = %{version}
Provides:       crate(%{pkgname}/cfsocket) = %{version}
Provides:       crate(%{pkgname}/cfstream) = %{version}
Provides:       crate(%{pkgname}/cfstring) = %{version}
Provides:       crate(%{pkgname}/cfstringtokenizer) = %{version}
Provides:       crate(%{pkgname}/cfurl) = %{version}
Provides:       crate(%{pkgname}/cfurlenumerator) = %{version}
Provides:       crate(%{pkgname}/cfxmlparser) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CFCalendar", "CFData", "CFDate", "CFDateFormatter", "CFFileSecurity", "CFNumberFormatter", "CFPropertyList", "CFRunLoop", "CFSocket", "CFStream", "CFString", "CFStringTokenizer", "CFURL", "CFURLEnumerator", and "CFXMLParser" features.

%package     -n %{name}+block2
Summary:        Bindings to the CoreFoundation framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreFoundation framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/cfarray) = %{version}
Requires:       crate(%{pkgname}/cfattributedstring) = %{version}
Requires:       crate(%{pkgname}/cfavailability) = %{version}
Requires:       crate(%{pkgname}/cfbag) = %{version}
Requires:       crate(%{pkgname}/cfbinaryheap) = %{version}
Requires:       crate(%{pkgname}/cfbitvector) = %{version}
Requires:       crate(%{pkgname}/cfbundle) = %{version}
Requires:       crate(%{pkgname}/cfbyteorder) = %{version}
Requires:       crate(%{pkgname}/cfcalendar) = %{version}
Requires:       crate(%{pkgname}/cfcgtypes) = %{version}
Requires:       crate(%{pkgname}/cfcharacterset) = %{version}
Requires:       crate(%{pkgname}/cfdata) = %{version}
Requires:       crate(%{pkgname}/cfdate) = %{version}
Requires:       crate(%{pkgname}/cfdateformatter) = %{version}
Requires:       crate(%{pkgname}/cfdictionary) = %{version}
Requires:       crate(%{pkgname}/cferror) = %{version}
Requires:       crate(%{pkgname}/cffiledescriptor) = %{version}
Requires:       crate(%{pkgname}/cffilesecurity) = %{version}
Requires:       crate(%{pkgname}/cflocale) = %{version}
Requires:       crate(%{pkgname}/cfmachport) = %{version}
Requires:       crate(%{pkgname}/cfmessageport) = %{version}
Requires:       crate(%{pkgname}/cfnotificationcenter) = %{version}
Requires:       crate(%{pkgname}/cfnumber) = %{version}
Requires:       crate(%{pkgname}/cfnumberformatter) = %{version}
Requires:       crate(%{pkgname}/cfplugin) = %{version}
Requires:       crate(%{pkgname}/cfplugincom) = %{version}
Requires:       crate(%{pkgname}/cfpreferences) = %{version}
Requires:       crate(%{pkgname}/cfpropertylist) = %{version}
Requires:       crate(%{pkgname}/cfrunloop) = %{version}
Requires:       crate(%{pkgname}/cfset) = %{version}
Requires:       crate(%{pkgname}/cfsocket) = %{version}
Requires:       crate(%{pkgname}/cfstream) = %{version}
Requires:       crate(%{pkgname}/cfstring) = %{version}
Requires:       crate(%{pkgname}/cfstringencodingext) = %{version}
Requires:       crate(%{pkgname}/cfstringtokenizer) = %{version}
Requires:       crate(%{pkgname}/cftimezone) = %{version}
Requires:       crate(%{pkgname}/cftree) = %{version}
Requires:       crate(%{pkgname}/cfurl) = %{version}
Requires:       crate(%{pkgname}/cfurlaccess) = %{version}
Requires:       crate(%{pkgname}/cfurlenumerator) = %{version}
Requires:       crate(%{pkgname}/cfusernotification) = %{version}
Requires:       crate(%{pkgname}/cfutilities) = %{version}
Requires:       crate(%{pkgname}/cfuuid) = %{version}
Requires:       crate(%{pkgname}/cfxmlnode) = %{version}
Requires:       crate(%{pkgname}/cfxmlparser) = %{version}
Requires:       crate(%{pkgname}/dispatch2) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/objc2) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the CoreFoundation framework - feature "dispatch2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Provides:       crate(%{pkgname}/dispatch2) = %{version}

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the CoreFoundation framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the CoreFoundation framework - feature "objc2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.0
Requires:       crate(objc2-0.6/std) >= 0.6.2
Provides:       crate(%{pkgname}/objc2) = %{version}

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
