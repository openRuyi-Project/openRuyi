# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deadpool
%global full_version 0.13.0
%global pkgname deadpool-0.13

Name:           rust-deadpool-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "deadpool"
License:        MIT OR Apache-2.0
URL:            https://github.com/deadpool-rs/deadpool
#!RemoteAsset:  sha256:883466cb8db62725aee5f4a6011e8a5d42912b42632df32aad57fc91127c6e04
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(deadpool-runtime-0.3/default) >= 0.3.1
Requires:       crate(num-cpus-1.0/default) >= 1.17.0
Requires:       crate(tokio-1.52.3/default) >= 1.52.3
Requires:       crate(tokio-1.52.3/sync) >= 1.52.3
Provides:       crate(deadpool) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/managed)
Provides:       crate(%{pkgname}/unmanaged)

%description
Source code for takopackized Rust crate "deadpool"

%package     -n %{name}+default
Summary:        Dead simple async pool - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/managed)
Requires:       crate(%{pkgname}/unmanaged)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-async-std-1
Summary:        Dead simple async pool - feature "rt_async-std_1"
Requires:       crate(%{pkgname})
Requires:       crate(deadpool-runtime-0.3/async-std-1) >= 0.3.1
Provides:       crate(%{pkgname}/rt-async-std-1)

%description -n %{name}+rt-async-std-1
This metapackage enables feature "rt_async-std_1" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-smol-2
Summary:        Dead simple async pool - feature "rt_smol_2"
Requires:       crate(%{pkgname})
Requires:       crate(deadpool-runtime-0.3/smol-2) >= 0.3.1
Provides:       crate(%{pkgname}/rt-smol-2)

%description -n %{name}+rt-smol-2
This metapackage enables feature "rt_smol_2" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-tokio-1
Summary:        Dead simple async pool - feature "rt_tokio_1"
Requires:       crate(%{pkgname})
Requires:       crate(deadpool-runtime-0.3/tokio-1) >= 0.3.1
Provides:       crate(%{pkgname}/rt-tokio-1)

%description -n %{name}+rt-tokio-1
This metapackage enables feature "rt_tokio_1" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Dead simple async pool - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.103
Requires:       crate(serde-1.0/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
