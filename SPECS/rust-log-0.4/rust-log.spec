# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name log
%global full_version 0.4.29
%global pkgname log-0.4

Name:           rust-log-0.4
Version:        0.4.29
Release:        %autorelease
Summary:        Rust crate "log"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/log
#!RemoteAsset:  sha256:5e5032e24019045c762d3c0f28f5b6b8bbf38563a65908389bf7978758920897
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/kv)
Provides:       crate(%{pkgname}/max-level-debug)
Provides:       crate(%{pkgname}/max-level-error)
Provides:       crate(%{pkgname}/max-level-info)
Provides:       crate(%{pkgname}/max-level-off)
Provides:       crate(%{pkgname}/max-level-trace)
Provides:       crate(%{pkgname}/max-level-warn)
Provides:       crate(%{pkgname}/release-max-level-debug)
Provides:       crate(%{pkgname}/release-max-level-error)
Provides:       crate(%{pkgname}/release-max-level-info)
Provides:       crate(%{pkgname}/release-max-level-off)
Provides:       crate(%{pkgname}/release-max-level-trace)
Provides:       crate(%{pkgname}/release-max-level-warn)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "log"

%package     -n %{name}+kv-serde
Summary:        Lightweight logging facade for Rust - feature "kv_serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kv-std)
Requires:       crate(%{pkgname}/serde)
Requires:       crate(value-bag-1.0/inline-i128) >= 1.12
Requires:       crate(value-bag-1.0/serde) >= 1.12
Provides:       crate(%{pkgname}/kv-serde)

%description -n %{name}+kv-serde
This metapackage enables feature "kv_serde" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-std
Summary:        Lightweight logging facade for Rust - feature "kv_std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kv)
Requires:       crate(%{pkgname}/std)
Requires:       crate(value-bag-1.0/error) >= 1.12
Requires:       crate(value-bag-1.0/inline-i128) >= 1.12
Provides:       crate(%{pkgname}/kv-std)

%description -n %{name}+kv-std
This metapackage enables feature "kv_std" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-sval
Summary:        Lightweight logging facade for Rust - feature "kv_sval"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kv)
Requires:       crate(%{pkgname}/sval)
Requires:       crate(%{pkgname}/sval-ref)
Requires:       crate(value-bag-1.0/inline-i128) >= 1.12
Requires:       crate(value-bag-1.0/sval) >= 1.12
Provides:       crate(%{pkgname}/kv-sval)

%description -n %{name}+kv-sval
This metapackage enables feature "kv_sval" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable
Summary:        Lightweight logging facade for Rust - feature "kv_unstable"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kv)
Requires:       crate(%{pkgname}/value-bag)
Provides:       crate(%{pkgname}/kv-unstable)

%description -n %{name}+kv-unstable
This metapackage enables feature "kv_unstable" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable-serde
Summary:        Lightweight logging facade for Rust - feature "kv_unstable_serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kv-serde)
Requires:       crate(%{pkgname}/kv-unstable-std)
Provides:       crate(%{pkgname}/kv-unstable-serde)

%description -n %{name}+kv-unstable-serde
This metapackage enables feature "kv_unstable_serde" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable-std
Summary:        Lightweight logging facade for Rust - feature "kv_unstable_std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kv-std)
Requires:       crate(%{pkgname}/kv-unstable)
Provides:       crate(%{pkgname}/kv-unstable-std)

%description -n %{name}+kv-unstable-std
This metapackage enables feature "kv_unstable_std" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable-sval
Summary:        Lightweight logging facade for Rust - feature "kv_unstable_sval"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kv-sval)
Requires:       crate(%{pkgname}/kv-unstable)
Provides:       crate(%{pkgname}/kv-unstable-sval)

%description -n %{name}+kv-unstable-sval
This metapackage enables feature "kv_unstable_sval" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-core
Summary:        Lightweight logging facade for Rust - feature "serde_core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serde-core)

%description -n %{name}+serde-core
This metapackage enables feature "serde_core" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde" feature.

%package     -n %{name}+sval
Summary:        Lightweight logging facade for Rust - feature "sval"
Requires:       crate(%{pkgname})
Requires:       crate(sval-2.0) >= 2.16
Provides:       crate(%{pkgname}/sval)

%description -n %{name}+sval
This metapackage enables feature "sval" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sval-ref
Summary:        Lightweight logging facade for Rust - feature "sval_ref"
Requires:       crate(%{pkgname})
Requires:       crate(sval-ref-2.0) >= 2.16
Provides:       crate(%{pkgname}/sval-ref)

%description -n %{name}+sval-ref
This metapackage enables feature "sval_ref" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+value-bag
Summary:        Lightweight logging facade for Rust - feature "value-bag"
Requires:       crate(%{pkgname})
Requires:       crate(value-bag-1.0/inline-i128) >= 1.12
Provides:       crate(%{pkgname}/value-bag)

%description -n %{name}+value-bag
This metapackage enables feature "value-bag" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
