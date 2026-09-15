# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heapless
%global full_version 0.9.3
%global pkgname heapless-0.9

Name:           rust-heapless-0.9
Version:        0.9.3
Release:        %autorelease
Summary:        Rust crate "heapless"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/heapless
#!RemoteAsset:  sha256:25ba4bd83f9415b58b4ed8dc5714c76e626a105be4646c02630ad730ad3b5aa4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hash32-0.3/default) >= 0.3.0
Requires:       crate(stable-deref-trait-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/mpmc-large) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for the Rust crate "heapless"

%package     -n %{name}+bytes
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+defmt
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "defmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/defmt) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+embedded-io-v0.7
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "embedded-io-v0.7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embedded-io-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/embedded-io-v0.7) = %{version}

%description -n %{name}+embedded-io-v0.7
This metapackage enables feature "embedded-io-v0.7" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-critical-section
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "portable-atomic-critical-section"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/portable-atomic) = %{version}
Requires:       crate(portable-atomic-1/critical-section) >= 1.0.0
Requires:       crate(portable-atomic-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic-critical-section) = %{version}

%description -n %{name}+portable-atomic-critical-section
This metapackage enables feature "portable-atomic-critical-section" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-unsafe-assume-single-core
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "portable-atomic-unsafe-assume-single-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/portable-atomic) = %{version}
Requires:       crate(portable-atomic-1/default) >= 1.0.0
Requires:       crate(portable-atomic-1/unsafe-assume-single-core) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic-unsafe-assume-single-core) = %{version}

%description -n %{name}+portable-atomic-unsafe-assume-single-core
This metapackage enables feature "portable-atomic-unsafe-assume-single-core" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ufmt
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "ufmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ufmt-0.2/default) >= 0.2.0
Requires:       crate(ufmt-write-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/ufmt) = %{version}

%description -n %{name}+ufmt
This metapackage enables feature "ufmt" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/derive) >= 1.8.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-APACHE LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
