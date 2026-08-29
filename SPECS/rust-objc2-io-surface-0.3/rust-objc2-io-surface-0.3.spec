# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-io-surface
%global full_version 0.3.2
%global pkgname objc2-io-surface-0.3

Name:           rust-objc2-io-surface-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-io-surface"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:180788110936d59bab6bd83b6060ffdfffb3b922ba1396b312ae795e1de9d81d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/iosurface) = %{version}
Provides:       crate(%{pkgname}/iosurfaceapi) = %{version}
Provides:       crate(%{pkgname}/iosurfacebase) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-io-surface"

%package     -n %{name}+bitflags
Summary:        Bindings to the IOSurface framework - feature "bitflags" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/iosurfaceref) = %{version}
Provides:       crate(%{pkgname}/iosurfacetypes) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-io-surface crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "IOSurfaceRef", and "IOSurfaceTypes" features.

%package     -n %{name}+default
Summary:        Bindings to the IOSurface framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/iosurface) = %{version}
Requires:       crate(%{pkgname}/iosurfaceapi) = %{version}
Requires:       crate(%{pkgname}/iosurfacebase) = %{version}
Requires:       crate(%{pkgname}/iosurfaceref) = %{version}
Requires:       crate(%{pkgname}/iosurfacetypes) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/objc2) = %{version}
Requires:       crate(%{pkgname}/objc2-core-foundation) = %{version}
Requires:       crate(%{pkgname}/objc2-foundation) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-io-surface crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the IOSurface framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-io-surface crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the IOSurface framework - feature "objc2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc) = %{version}
Provides:       crate(%{pkgname}/objc2) = %{version}

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-io-surface crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ObjC" feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Bindings to the IOSurface framework - feature "objc2-core-foundation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-foundation) = %{version}

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust objc2-io-surface crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-foundation
Summary:        Bindings to the IOSurface framework - feature "objc2-foundation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-foundation) = %{version}

%description -n %{name}+objc2-foundation
This metapackage enables feature "objc2-foundation" for the Rust objc2-io-surface crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
