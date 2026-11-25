# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const_format
%global full_version 0.2.35
%global pkgname const-format-0.2

Name:           rust-const-format-0.2
Version:        0.2.35
Release:        %autorelease
Summary:        Rust crate "const_format"
License:        Zlib
URL:            https://github.com/rodrimati1992/const_format_crates/
#!RemoteAsset:  sha256:7faa7469a93a566e9ccc1c73fe783b4a65c274c5ace346038dca9c39fe0030ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-format-proc-macros-0.2/default) >= 0.2.34

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/assertcp) = %{version}
Provides:       crate(%{pkgname}/const-generics) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/docsrs) = %{version}
Provides:       crate(%{pkgname}/nightly-const-generics) = %{version}
Provides:       crate(%{pkgname}/only-new-tests) = %{version}
Provides:       crate(%{pkgname}/rust-1-51) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description
Source code for takopackized Rust crate "const_format"

%package     -n %{name}+debug
Summary:        Compile-time string formatting - feature "__debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-format-proc-macros-0.2/debug) >= 0.2.34
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "__debug" for the Rust const_format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inline-const-pat-tests
Summary:        Compile-time string formatting - feature "__inline_const_pat_tests"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fmt) = %{version}
Requires:       crate(%{pkgname}/test) = %{version}
Provides:       crate(%{pkgname}/inline-const-pat-tests) = %{version}

%description -n %{name}+inline-const-pat-tests
This metapackage enables feature "__inline_const_pat_tests" for the Rust const_format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Compile-time string formatting - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/assert) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/fmt) = %{version}
Requires:       crate(%{pkgname}/rust-1-64) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust const_format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+assertc
Summary:        Compile-time string formatting - feature "assertc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/assertcp) = %{version}
Requires:       crate(%{pkgname}/fmt) = %{version}
Provides:       crate(%{pkgname}/assert) = %{version}
Provides:       crate(%{pkgname}/assertc) = %{version}

%description -n %{name}+assertc
This metapackage enables feature "assertc" for the Rust const_format crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "assert" feature.

%package     -n %{name}+derive
Summary:        Compile-time string formatting - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fmt) = %{version}
Requires:       crate(const-format-proc-macros-0.2/derive) >= 0.2.34
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust const_format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+konst
Summary:        Compile-time string formatting - feature "konst"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(konst-0.2) >= 0.2.13
Provides:       crate(%{pkgname}/konst) = %{version}

%description -n %{name}+konst
This metapackage enables feature "konst" for the Rust const_format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-1-64
Summary:        Compile-time string formatting - feature "rust_1_64" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/konst) = %{version}
Requires:       crate(%{pkgname}/rust-1-51) = %{version}
Requires:       crate(konst-0.2/rust-1-64) >= 0.2.13
Provides:       crate(%{pkgname}/constant-time-as-str) = %{version}
Provides:       crate(%{pkgname}/fmt) = %{version}
Provides:       crate(%{pkgname}/more-str-macros) = %{version}
Provides:       crate(%{pkgname}/rust-1-64) = %{version}
Provides:       crate(%{pkgname}/rust-1-83) = %{version}

%description -n %{name}+rust-1-64
This metapackage enables feature "rust_1_64" for the Rust const_format crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "constant_time_as_str", "fmt", "more_str_macros", and "rust_1_83" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
