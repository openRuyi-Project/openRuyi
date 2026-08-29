# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name log
%global full_version 0.4.30
%global pkgname log-0.4

Name:           rust-log-0.4
Version:        0.4.30
Release:        %autorelease
Summary:        Rust crate "log"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/log
#!RemoteAsset:  sha256:616ec5685824bcc94416c6d4a7a446eea774a31efd7062c8480ba6fd06d7a6e5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/kv) = %{version}
Provides:       crate(%{pkgname}/max-level-debug) = %{version}
Provides:       crate(%{pkgname}/max-level-error) = %{version}
Provides:       crate(%{pkgname}/max-level-info) = %{version}
Provides:       crate(%{pkgname}/max-level-off) = %{version}
Provides:       crate(%{pkgname}/max-level-trace) = %{version}
Provides:       crate(%{pkgname}/max-level-warn) = %{version}
Provides:       crate(%{pkgname}/release-max-level-debug) = %{version}
Provides:       crate(%{pkgname}/release-max-level-error) = %{version}
Provides:       crate(%{pkgname}/release-max-level-info) = %{version}
Provides:       crate(%{pkgname}/release-max-level-off) = %{version}
Provides:       crate(%{pkgname}/release-max-level-trace) = %{version}
Provides:       crate(%{pkgname}/release-max-level-warn) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "log"

%package     -n %{name}+kv-serde
Summary:        Lightweight logging facade for Rust - feature "kv_serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kv-std) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(value-bag-1/inline-i128) >= 1.12.0
Requires:       crate(value-bag-1/serde) >= 1.12.0
Provides:       crate(%{pkgname}/kv-serde) = %{version}

%description -n %{name}+kv-serde
This metapackage enables feature "kv_serde" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-std
Summary:        Lightweight logging facade for Rust - feature "kv_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kv) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(value-bag-1/error) >= 1.12.0
Requires:       crate(value-bag-1/inline-i128) >= 1.12.0
Provides:       crate(%{pkgname}/kv-std) = %{version}

%description -n %{name}+kv-std
This metapackage enables feature "kv_std" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-sval
Summary:        Lightweight logging facade for Rust - feature "kv_sval"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kv) = %{version}
Requires:       crate(%{pkgname}/sval) = %{version}
Requires:       crate(%{pkgname}/sval-ref) = %{version}
Requires:       crate(value-bag-1/inline-i128) >= 1.12.0
Requires:       crate(value-bag-1/sval) >= 1.12.0
Provides:       crate(%{pkgname}/kv-sval) = %{version}

%description -n %{name}+kv-sval
This metapackage enables feature "kv_sval" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable
Summary:        Lightweight logging facade for Rust - feature "kv_unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kv) = %{version}
Requires:       crate(%{pkgname}/value-bag) = %{version}
Provides:       crate(%{pkgname}/kv-unstable) = %{version}

%description -n %{name}+kv-unstable
This metapackage enables feature "kv_unstable" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable-serde
Summary:        Lightweight logging facade for Rust - feature "kv_unstable_serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kv-serde) = %{version}
Requires:       crate(%{pkgname}/kv-unstable-std) = %{version}
Provides:       crate(%{pkgname}/kv-unstable-serde) = %{version}

%description -n %{name}+kv-unstable-serde
This metapackage enables feature "kv_unstable_serde" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable-std
Summary:        Lightweight logging facade for Rust - feature "kv_unstable_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kv-std) = %{version}
Requires:       crate(%{pkgname}/kv-unstable) = %{version}
Provides:       crate(%{pkgname}/kv-unstable-std) = %{version}

%description -n %{name}+kv-unstable-std
This metapackage enables feature "kv_unstable_std" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-unstable-sval
Summary:        Lightweight logging facade for Rust - feature "kv_unstable_sval"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kv-sval) = %{version}
Requires:       crate(%{pkgname}/kv-unstable) = %{version}
Provides:       crate(%{pkgname}/kv-unstable-sval) = %{version}

%description -n %{name}+kv-unstable-sval
This metapackage enables feature "kv_unstable_sval" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-core
Summary:        Lightweight logging facade for Rust - feature "serde_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-core) = %{version}

%description -n %{name}+serde-core
This metapackage enables feature "serde_core" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde" feature.

%package     -n %{name}+sval
Summary:        Lightweight logging facade for Rust - feature "sval"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-2) >= 2.16.0
Provides:       crate(%{pkgname}/sval) = %{version}

%description -n %{name}+sval
This metapackage enables feature "sval" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sval-ref
Summary:        Lightweight logging facade for Rust - feature "sval_ref"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-ref-2) >= 2.16.0
Provides:       crate(%{pkgname}/sval-ref) = %{version}

%description -n %{name}+sval-ref
This metapackage enables feature "sval_ref" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+value-bag
Summary:        Lightweight logging facade for Rust - feature "value-bag"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(value-bag-1/inline-i128) >= 1.12.0
Provides:       crate(%{pkgname}/value-bag) = %{version}

%description -n %{name}+value-bag
This metapackage enables feature "value-bag" for the Rust log crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
