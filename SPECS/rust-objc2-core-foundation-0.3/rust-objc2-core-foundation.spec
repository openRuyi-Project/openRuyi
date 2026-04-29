# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cfarray)
Provides:       crate(%{pkgname}/cfattributedstring)
Provides:       crate(%{pkgname}/cfavailability)
Provides:       crate(%{pkgname}/cfbag)
Provides:       crate(%{pkgname}/cfbase)
Provides:       crate(%{pkgname}/cfbinaryheap)
Provides:       crate(%{pkgname}/cfbitvector)
Provides:       crate(%{pkgname}/cfbundle)
Provides:       crate(%{pkgname}/cfbyteorder)
Provides:       crate(%{pkgname}/cfcgtypes)
Provides:       crate(%{pkgname}/cfcharacterset)
Provides:       crate(%{pkgname}/cfdictionary)
Provides:       crate(%{pkgname}/cferror)
Provides:       crate(%{pkgname}/cffiledescriptor)
Provides:       crate(%{pkgname}/cflocale)
Provides:       crate(%{pkgname}/cfmachport)
Provides:       crate(%{pkgname}/cfmessageport)
Provides:       crate(%{pkgname}/cfnotificationcenter)
Provides:       crate(%{pkgname}/cfnumber)
Provides:       crate(%{pkgname}/cfplugin)
Provides:       crate(%{pkgname}/cfplugincom)
Provides:       crate(%{pkgname}/cfpreferences)
Provides:       crate(%{pkgname}/cfset)
Provides:       crate(%{pkgname}/cfstringencodingext)
Provides:       crate(%{pkgname}/cftimezone)
Provides:       crate(%{pkgname}/cftree)
Provides:       crate(%{pkgname}/cfurlaccess)
Provides:       crate(%{pkgname}/cfuuid)
Provides:       crate(%{pkgname}/cfusernotification)
Provides:       crate(%{pkgname}/cfutilities)
Provides:       crate(%{pkgname}/cfxmlnode)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-coerce-pointee)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-foundation"

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreFoundation framework - feature "bitflags" and 15 more
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/std) >= 2.11.0
Provides:       crate(%{pkgname}/bitflags)
Provides:       crate(%{pkgname}/cfcalendar)
Provides:       crate(%{pkgname}/cfdata)
Provides:       crate(%{pkgname}/cfdate)
Provides:       crate(%{pkgname}/cfdateformatter)
Provides:       crate(%{pkgname}/cffilesecurity)
Provides:       crate(%{pkgname}/cfnumberformatter)
Provides:       crate(%{pkgname}/cfpropertylist)
Provides:       crate(%{pkgname}/cfrunloop)
Provides:       crate(%{pkgname}/cfsocket)
Provides:       crate(%{pkgname}/cfstream)
Provides:       crate(%{pkgname}/cfstring)
Provides:       crate(%{pkgname}/cfstringtokenizer)
Provides:       crate(%{pkgname}/cfurl)
Provides:       crate(%{pkgname}/cfurlenumerator)
Provides:       crate(%{pkgname}/cfxmlparser)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CFCalendar", "CFData", "CFDate", "CFDateFormatter", "CFFileSecurity", "CFNumberFormatter", "CFPropertyList", "CFRunLoop", "CFSocket", "CFStream", "CFString", "CFStringTokenizer", "CFURL", "CFURLEnumerator", and "CFXMLParser" features.

%package     -n %{name}+block2
Summary:        Bindings to the CoreFoundation framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreFoundation framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/cfarray)
Requires:       crate(%{pkgname}/cfattributedstring)
Requires:       crate(%{pkgname}/cfavailability)
Requires:       crate(%{pkgname}/cfbag)
Requires:       crate(%{pkgname}/cfbinaryheap)
Requires:       crate(%{pkgname}/cfbitvector)
Requires:       crate(%{pkgname}/cfbundle)
Requires:       crate(%{pkgname}/cfbyteorder)
Requires:       crate(%{pkgname}/cfcalendar)
Requires:       crate(%{pkgname}/cfcgtypes)
Requires:       crate(%{pkgname}/cfcharacterset)
Requires:       crate(%{pkgname}/cfdata)
Requires:       crate(%{pkgname}/cfdate)
Requires:       crate(%{pkgname}/cfdateformatter)
Requires:       crate(%{pkgname}/cfdictionary)
Requires:       crate(%{pkgname}/cferror)
Requires:       crate(%{pkgname}/cffiledescriptor)
Requires:       crate(%{pkgname}/cffilesecurity)
Requires:       crate(%{pkgname}/cflocale)
Requires:       crate(%{pkgname}/cfmachport)
Requires:       crate(%{pkgname}/cfmessageport)
Requires:       crate(%{pkgname}/cfnotificationcenter)
Requires:       crate(%{pkgname}/cfnumber)
Requires:       crate(%{pkgname}/cfnumberformatter)
Requires:       crate(%{pkgname}/cfplugin)
Requires:       crate(%{pkgname}/cfplugincom)
Requires:       crate(%{pkgname}/cfpreferences)
Requires:       crate(%{pkgname}/cfpropertylist)
Requires:       crate(%{pkgname}/cfrunloop)
Requires:       crate(%{pkgname}/cfset)
Requires:       crate(%{pkgname}/cfsocket)
Requires:       crate(%{pkgname}/cfstream)
Requires:       crate(%{pkgname}/cfstring)
Requires:       crate(%{pkgname}/cfstringencodingext)
Requires:       crate(%{pkgname}/cfstringtokenizer)
Requires:       crate(%{pkgname}/cftimezone)
Requires:       crate(%{pkgname}/cftree)
Requires:       crate(%{pkgname}/cfurl)
Requires:       crate(%{pkgname}/cfurlaccess)
Requires:       crate(%{pkgname}/cfurlenumerator)
Requires:       crate(%{pkgname}/cfusernotification)
Requires:       crate(%{pkgname}/cfutilities)
Requires:       crate(%{pkgname}/cfuuid)
Requires:       crate(%{pkgname}/cfxmlnode)
Requires:       crate(%{pkgname}/cfxmlparser)
Requires:       crate(%{pkgname}/dispatch2)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/objc2)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the CoreFoundation framework - feature "dispatch2"
Requires:       crate(%{pkgname})
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.1
Provides:       crate(%{pkgname}/dispatch2)

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the CoreFoundation framework - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the CoreFoundation framework - feature "objc2"
Requires:       crate(%{pkgname})
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.1
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.1
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/objc2)

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-core-foundation crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
