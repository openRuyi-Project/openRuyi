# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memsec
%global full_version 0.5.7
%global pkgname memsec-0.5

Name:           rust-memsec-0.5
Version:        0.5.7
Release:        %autorelease
Summary:        Rust crate "memsec"
License:        MIT
URL:            https://github.com/quininer/memsec
#!RemoteAsset:  sha256:0cb9280f8c37546661083aa45eb0318d8469253d31e87649faed25522428398e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "memsec"

%package     -n %{name}+default
Summary:        Rust implementation `libsodium/utils` - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/use-os) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust memsec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Rust implementation `libsodium/utils` - feature "getrandom" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust memsec crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "alloc" feature.

%package     -n %{name}+libc
Summary:        Rust implementation `libsodium/utils` - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust memsec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mach-o-sys
Summary:        Rust implementation `libsodium/utils` - feature "mach_o_sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mach-o-sys-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/mach-o-sys) = %{version}

%description -n %{name}+mach-o-sys
This metapackage enables feature "mach_o_sys" for the Rust memsec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-os
Summary:        Rust implementation `libsodium/utils` - feature "use_os"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/mach-o-sys) = %{version}
Requires:       crate(%{pkgname}/winapi) = %{version}
Provides:       crate(%{pkgname}/use-os) = %{version}

%description -n %{name}+use-os
This metapackage enables feature "use_os" for the Rust memsec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+winapi
Summary:        Rust implementation `libsodium/utils` - feature "winapi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/memoryapi) >= 0.3.0
Requires:       crate(winapi-0.3/sysinfoapi) >= 0.3.0
Provides:       crate(%{pkgname}/winapi) = %{version}

%description -n %{name}+winapi
This metapackage enables feature "winapi" for the Rust memsec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
