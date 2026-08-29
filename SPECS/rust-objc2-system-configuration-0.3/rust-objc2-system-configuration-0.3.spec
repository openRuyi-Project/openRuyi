# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-system-configuration
%global full_version 0.3.2
%global pkgname objc2-system-configuration-0.3

Name:           rust-objc2-system-configuration-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-system-configuration"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:7216bd11cbda54ccabcab84d523dc93b858ec75ecfb3a7d89513fa22464da396
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/dhcpclientpreferences) = %{version}
Provides:       crate(%{pkgname}/scdynamicstorekey) = %{version}
Provides:       crate(%{pkgname}/scnetwork) = %{version}
Provides:       crate(%{pkgname}/scschemadefinitions) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-system-configuration"

%package     -n %{name}+captivenetwork
Summary:        Bindings to the SystemConfiguration framework - feature "CaptiveNetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}/captivenetwork) = %{version}

%description -n %{name}+captivenetwork
This metapackage enables feature "CaptiveNetwork" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scdynamicstore
Summary:        Bindings to the SystemConfiguration framework - feature "SCDynamicStore"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Provides:       crate(%{pkgname}/scdynamicstore) = %{version}

%description -n %{name}+scdynamicstore
This metapackage enables feature "SCDynamicStore" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scdynamicstorecopydhcpinfo
Summary:        Bindings to the SystemConfiguration framework - feature "SCDynamicStoreCopyDHCPInfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}/scdynamicstorecopydhcpinfo) = %{version}

%description -n %{name}+scdynamicstorecopydhcpinfo
This metapackage enables feature "SCDynamicStoreCopyDHCPInfo" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scdynamicstorecopyspecific
Summary:        Bindings to the SystemConfiguration framework - feature "SCDynamicStoreCopySpecific"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstring) >= 0.3.2
Provides:       crate(%{pkgname}/scdynamicstorecopyspecific) = %{version}

%description -n %{name}+scdynamicstorecopyspecific
This metapackage enables feature "SCDynamicStoreCopySpecific" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scnetworkconfiguration
Summary:        Bindings to the SystemConfiguration framework - feature "SCNetworkConfiguration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfnumber) >= 0.3.2
Provides:       crate(%{pkgname}/scnetworkconfiguration) = %{version}

%description -n %{name}+scnetworkconfiguration
This metapackage enables feature "SCNetworkConfiguration" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scnetworkconnection
Summary:        Bindings to the SystemConfiguration framework - feature "SCNetworkConnection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Provides:       crate(%{pkgname}/scnetworkconnection) = %{version}

%description -n %{name}+scnetworkconnection
This metapackage enables feature "SCNetworkConnection" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scnetworkreachability
Summary:        Bindings to the SystemConfiguration framework - feature "SCNetworkReachability"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Provides:       crate(%{pkgname}/scnetworkreachability) = %{version}

%description -n %{name}+scnetworkreachability
This metapackage enables feature "SCNetworkReachability" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scpreferences
Summary:        Bindings to the SystemConfiguration framework - feature "SCPreferences"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Provides:       crate(%{pkgname}/scpreferences) = %{version}

%description -n %{name}+scpreferences
This metapackage enables feature "SCPreferences" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scpreferencespath
Summary:        Bindings to the SystemConfiguration framework - feature "SCPreferencesPath"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}/scpreferencespath) = %{version}

%description -n %{name}+scpreferencespath
This metapackage enables feature "SCPreferencesPath" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scpreferencessetspecific
Summary:        Bindings to the SystemConfiguration framework - feature "SCPreferencesSetSpecific"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstring) >= 0.3.2
Provides:       crate(%{pkgname}/scpreferencessetspecific) = %{version}

%description -n %{name}+scpreferencessetspecific
This metapackage enables feature "SCPreferencesSetSpecific" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the SystemConfiguration framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the SystemConfiguration framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/captivenetwork) = %{version}
Requires:       crate(%{pkgname}/dhcpclientpreferences) = %{version}
Requires:       crate(%{pkgname}/dispatch2) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/objc2) = %{version}
Requires:       crate(%{pkgname}/objc2-security) = %{version}
Requires:       crate(%{pkgname}/scdynamicstore) = %{version}
Requires:       crate(%{pkgname}/scdynamicstorecopydhcpinfo) = %{version}
Requires:       crate(%{pkgname}/scdynamicstorecopyspecific) = %{version}
Requires:       crate(%{pkgname}/scdynamicstorekey) = %{version}
Requires:       crate(%{pkgname}/scnetwork) = %{version}
Requires:       crate(%{pkgname}/scnetworkconfiguration) = %{version}
Requires:       crate(%{pkgname}/scnetworkconnection) = %{version}
Requires:       crate(%{pkgname}/scnetworkreachability) = %{version}
Requires:       crate(%{pkgname}/scpreferences) = %{version}
Requires:       crate(%{pkgname}/scpreferencespath) = %{version}
Requires:       crate(%{pkgname}/scpreferencessetspecific) = %{version}
Requires:       crate(%{pkgname}/scschemadefinitions) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the SystemConfiguration framework - feature "dispatch2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Provides:       crate(%{pkgname}/dispatch2) = %{version}

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the SystemConfiguration framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the SystemConfiguration framework - feature "objc2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.0
Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Requires:       crate(objc2-security-0.3/authorization) >= 0.3.2
Requires:       crate(objc2-security-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2) = %{version}

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-security
Summary:        Bindings to the SystemConfiguration framework - feature "objc2-security"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-security-0.3/authorization) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-security) = %{version}

%description -n %{name}+objc2-security
This metapackage enables feature "objc2-security" for the Rust objc2-system-configuration crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
