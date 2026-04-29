# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libredox
%global full_version 0.1.15
%global pkgname libredox-0.1

Name:           rust-libredox-0.1
Version:        0.1.15
Release:        %autorelease
Summary:        Rust crate "libredox"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/libredox.git
#!RemoteAsset:  sha256:7ddbf48fd451246b1f8c2610bd3b4ac0cc6e149d89832867093ab69a17194f08
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "libredox"

%package     -n %{name}+bitflags
Summary:        Redox stable ABI - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/default) >= 2.11.0
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Redox stable ABI - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/base)
Requires:       crate(%{pkgname}/call)
Requires:       crate(%{pkgname}/protocol)
Requires:       crate(%{pkgname}/redox-syscall)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ioslice
Summary:        Redox stable ABI - feature "ioslice" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(ioslice-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/ioslice)
Provides:       crate(%{pkgname}/mkns)

%description -n %{name}+ioslice
This metapackage enables feature "ioslice" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mkns" feature.

%package     -n %{name}+libc
Summary:        Redox stable ABI - feature "libc" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname}/base)
Provides:       crate(%{pkgname}/call)
Provides:       crate(%{pkgname}/libc)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "base", "call", and "std" features.

%package     -n %{name}+plain
Summary:        Redox stable ABI - feature "plain"
Requires:       crate(%{pkgname})
Requires:       crate(plain-0.2/default) >= 0.2.3
Provides:       crate(%{pkgname}/plain)

%description -n %{name}+plain
This metapackage enables feature "plain" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+protocol
Summary:        Redox stable ABI - feature "protocol"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/plain)
Requires:       crate(%{pkgname}/redox-syscall)
Provides:       crate(%{pkgname}/protocol)

%description -n %{name}+protocol
This metapackage enables feature "protocol" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+redox-syscall
Summary:        Redox stable ABI - feature "redox_syscall"
Requires:       crate(%{pkgname})
Requires:       crate(redox-syscall-0.7/default) >= 0.7.3
Provides:       crate(%{pkgname}/redox-syscall)

%description -n %{name}+redox-syscall
This metapackage enables feature "redox_syscall" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
