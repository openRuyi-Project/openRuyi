# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libredox
%global full_version 0.1.17
%global pkgname libredox-0.1

Name:           rust-libredox-0.1
Version:        0.1.17
Release:        %autorelease
Summary:        Rust crate "libredox"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/libredox.git
#!RemoteAsset:  sha256:f02ab6bace2054fb888a3c16f990117b579d14a3088e472d63c6011fa185c9d3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "libredox"

%package     -n %{name}+bitflags
Summary:        Redox stable ABI - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Redox stable ABI - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base) = %{version}
Requires:       crate(%{pkgname}/call) = %{version}
Requires:       crate(%{pkgname}/protocol) = %{version}
Requires:       crate(%{pkgname}/redox-syscall) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ioslice
Summary:        Redox stable ABI - feature "ioslice" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ioslice-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/ioslice) = %{version}
Provides:       crate(%{pkgname}/mkns) = %{version}

%description -n %{name}+ioslice
This metapackage enables feature "ioslice" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mkns" feature.

%package     -n %{name}+libc
Summary:        Redox stable ABI - feature "libc" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/base) = %{version}
Provides:       crate(%{pkgname}/call) = %{version}
Provides:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "base", "call", and "std" features.

%package     -n %{name}+plain
Summary:        Redox stable ABI - feature "plain"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(plain-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/plain) = %{version}

%description -n %{name}+plain
This metapackage enables feature "plain" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+protocol
Summary:        Redox stable ABI - feature "protocol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/plain) = %{version}
Requires:       crate(%{pkgname}/redox-syscall) = %{version}
Provides:       crate(%{pkgname}/protocol) = %{version}

%description -n %{name}+protocol
This metapackage enables feature "protocol" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+redox-syscall
Summary:        Redox stable ABI - feature "redox_syscall"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(redox-syscall-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/redox-syscall) = %{version}

%description -n %{name}+redox-syscall
This metapackage enables feature "redox_syscall" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
