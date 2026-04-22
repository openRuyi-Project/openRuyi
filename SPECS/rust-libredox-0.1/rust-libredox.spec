# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libredox
%global full_version 0.1.3
%global pkgname libredox-0.1

Name:           rust-libredox-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "libredox"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/libredox.git
#!RemoteAsset:  sha256:c0ff37bd590ca25063e35af745c343cb7a0271906fb7b37e4813e8f79f00268d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.7.0
Requires:       crate(libc-0.2/default) >= 0.2.169
Provides:       crate(libredox) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/call)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "libredox"

%package     -n %{name}+default
Summary:        Redox stable ABI - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/call)
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

%package     -n %{name}+redox-syscall
Summary:        Redox stable ABI - feature "redox_syscall"
Requires:       crate(%{pkgname})
Requires:       crate(redox-syscall-0.5/default) >= 0.5.3
Provides:       crate(%{pkgname}/redox-syscall)

%description -n %{name}+redox-syscall
This metapackage enables feature "redox_syscall" for the Rust libredox crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
