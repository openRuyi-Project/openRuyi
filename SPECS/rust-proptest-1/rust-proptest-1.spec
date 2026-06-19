# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proptest
%global full_version 1.11.0
%global pkgname proptest-1

Name:           rust-proptest-1
Version:        1.11.0
Release:        %autorelease
Summary:        Rust crate "proptest"
License:        MIT OR Apache-2.0
URL:            https://proptest-rs.github.io/proptest/proptest/index.html
#!RemoteAsset:  sha256:4b45fcc2344c680f5025fe57779faef368840d0bd1f42f216291f0dc4ace4744
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.10.0
Requires:       crate(num-traits-0.2) >= 0.2.15
Requires:       crate(rand-0.9/alloc) >= 0.9.0
Requires:       crate(rand-chacha-0.9) >= 0.9.0
Requires:       crate(rand-xorshift-0.4/default) >= 0.4.0
Requires:       crate(unarray-0.1/default) >= 0.1.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/atomic64bit) = %{version}
Provides:       crate(%{pkgname}/f16) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "proptest"

%package     -n %{name}+bit-set
Summary:        Hypothesis-like property-based testing and shrinking - feature "bit-set"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-set-0.8/default) >= 0.8.0
Requires:       crate(bit-vec-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/bit-set) = %{version}

%description -n %{name}+bit-set
This metapackage enables feature "bit-set" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Hypothesis-like property-based testing and shrinking - feature "default" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bit-set) = %{version}
Requires:       crate(%{pkgname}/fork) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/timeout) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/default-code-coverage) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default-code-coverage" feature.

%package     -n %{name}+fork
Summary:        Hypothesis-like property-based testing and shrinking - feature "fork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rusty-fork) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tempfile) = %{version}
Provides:       crate(%{pkgname}/fork) = %{version}

%description -n %{name}+fork
This metapackage enables feature "fork" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std
Summary:        Hypothesis-like property-based testing and shrinking - feature "no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/libm) >= 0.2.15
Provides:       crate(%{pkgname}/no-std) = %{version}

%description -n %{name}+no-std
This metapackage enables feature "no_std" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest-macro
Summary:        Hypothesis-like property-based testing and shrinking - feature "proptest-macro" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-macro-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/attr-macro) = %{version}
Provides:       crate(%{pkgname}/proptest-macro) = %{version}

%description -n %{name}+proptest-macro
This metapackage enables feature "proptest-macro" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "attr-macro" feature.

%package     -n %{name}+regex-syntax
Summary:        Hypothesis-like property-based testing and shrinking - feature "regex-syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/regex-syntax) = %{version}

%description -n %{name}+regex-syntax
This metapackage enables feature "regex-syntax" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rusty-fork
Summary:        Hypothesis-like property-based testing and shrinking - feature "rusty-fork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rusty-fork-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/rusty-fork) = %{version}

%description -n %{name}+rusty-fork
This metapackage enables feature "rusty-fork" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Hypothesis-like property-based testing and shrinking - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/regex-syntax) = %{version}
Requires:       crate(num-traits-0.2/std) >= 0.2.15
Requires:       crate(rand-0.9/alloc) >= 0.9.0
Requires:       crate(rand-0.9/os-rng) >= 0.9.0
Requires:       crate(rand-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/handle-panics) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "handle-panics" feature.

%package     -n %{name}+tempfile
Summary:        Hypothesis-like property-based testing and shrinking - feature "tempfile"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/tempfile) = %{version}

%description -n %{name}+tempfile
This metapackage enables feature "tempfile" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+timeout
Summary:        Hypothesis-like property-based testing and shrinking - feature "timeout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fork) = %{version}
Requires:       crate(rusty-fork-0.3/timeout) >= 0.3.0
Provides:       crate(%{pkgname}/timeout) = %{version}

%description -n %{name}+timeout
This metapackage enables feature "timeout" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+x86
Summary:        Hypothesis-like property-based testing and shrinking - feature "x86" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x86-0.52/default) >= 0.52.0
Provides:       crate(%{pkgname}/hardware-rng) = %{version}
Provides:       crate(%{pkgname}/x86) = %{version}

%description -n %{name}+x86
This metapackage enables feature "x86" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "hardware-rng" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
