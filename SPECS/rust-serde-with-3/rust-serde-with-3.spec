# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_with
%global full_version 3.20.0
%global pkgname serde-with-3

Name:           rust-serde-with-3
Version:        3.20.0
Release:        %autorelease
Summary:        Rust crate "serde_with"
License:        MIT OR Apache-2.0
URL:            https://github.com/jonasbb/serde_with/
#!RemoteAsset:  sha256:e72c1c2cb7b223fafb600a619537a871c2818583d619401b785e7c0b746ccde2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-core-1/result) >= 1.0.225
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "serde_with"

%package     -n %{name}+alloc
Summary:        Custom de/serialization functions for Rust's serde - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/alloc) >= 0.22.1
Requires:       crate(bs58-0.5/alloc) >= 0.5.1
Requires:       crate(chrono-0.4/alloc) >= 0.4.20
Requires:       crate(chrono-0.4/serde) >= 0.4.20
Requires:       crate(hex-0.4/alloc) >= 0.4.3
Requires:       crate(serde-core-1/alloc) >= 1.0.225
Requires:       crate(serde-core-1/result) >= 1.0.225
Requires:       crate(serde-json-1/alloc) >= 1.0.145
Requires:       crate(time-0.3/alloc) >= 0.3.47
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base58
Summary:        Custom de/serialization functions for Rust's serde - feature "base58"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bs58-0.5) >= 0.5.1
Provides:       crate(%{pkgname}/base58) = %{version}

%description -n %{name}+base58
This metapackage enables feature "base58" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Custom de/serialization functions for Rust's serde - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(base64-0.22) >= 0.22.1
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-0-4
Summary:        Custom de/serialization functions for Rust's serde - feature "chrono_0_4" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/serde) >= 0.4.20
Provides:       crate(%{pkgname}/chrono) = %{version}
Provides:       crate(%{pkgname}/chrono-0-4) = %{version}

%description -n %{name}+chrono-0-4
This metapackage enables feature "chrono_0_4" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "chrono" feature.

%package     -n %{name}+default
Summary:        Custom de/serialization functions for Rust's serde - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+guide
Summary:        Custom de/serialization functions for Rust's serde - feature "guide"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.7
Provides:       crate(%{pkgname}/guide) = %{version}

%description -n %{name}+guide
This metapackage enables feature "guide" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-14
Summary:        Custom de/serialization functions for Rust's serde - feature "hashbrown_0_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(hashbrown-0.14/serde) >= 0.14.0
Provides:       crate(%{pkgname}/hashbrown-0-14) = %{version}

%description -n %{name}+hashbrown-0-14
This metapackage enables feature "hashbrown_0_14" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-15
Summary:        Custom de/serialization functions for Rust's serde - feature "hashbrown_0_15"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(hashbrown-0.15/serde) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown-0-15) = %{version}

%description -n %{name}+hashbrown-0-15
This metapackage enables feature "hashbrown_0_15" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-16
Summary:        Custom de/serialization functions for Rust's serde - feature "hashbrown_0_16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(hashbrown-0.16/serde) >= 0.16.0
Provides:       crate(%{pkgname}/hashbrown-0-16) = %{version}

%description -n %{name}+hashbrown-0-16
This metapackage enables feature "hashbrown_0_16" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-17
Summary:        Custom de/serialization functions for Rust's serde - feature "hashbrown_0_17"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(hashbrown-0.17/serde) >= 0.17.0
Provides:       crate(%{pkgname}/hashbrown-0-17) = %{version}

%description -n %{name}+hashbrown-0-17
This metapackage enables feature "hashbrown_0_17" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex
Summary:        Custom de/serialization functions for Rust's serde - feature "hex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(hex-0.4) >= 0.4.3
Provides:       crate(%{pkgname}/hex) = %{version}

%description -n %{name}+hex
This metapackage enables feature "hex" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap-1
Summary:        Custom de/serialization functions for Rust's serde - feature "indexmap_1" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(indexmap-1/serde-1) >= 1.8.0
Provides:       crate(%{pkgname}/indexmap) = %{version}
Provides:       crate(%{pkgname}/indexmap-1) = %{version}

%description -n %{name}+indexmap-1
This metapackage enables feature "indexmap_1" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "indexmap" feature.

%package     -n %{name}+indexmap-2
Summary:        Custom de/serialization functions for Rust's serde - feature "indexmap_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(indexmap-2/serde) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap-2) = %{version}

%description -n %{name}+indexmap-2
This metapackage enables feature "indexmap_2" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Custom de/serialization functions for Rust's serde - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-json-1) >= 1.0.145
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Custom de/serialization functions for Rust's serde - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-with-macros-3/default) >= 3.20.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars-0-8
Summary:        Custom de/serialization functions for Rust's serde - feature "schemars_0_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(schemars-0.8) >= 0.8.16
Requires:       crate(serde-json-1) >= 1.0.145
Requires:       crate(serde-with-macros-3/schemars-0-8) >= 3.20.0
Provides:       crate(%{pkgname}/schemars-0-8) = %{version}

%description -n %{name}+schemars-0-8
This metapackage enables feature "schemars_0_8" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars-0-9
Summary:        Custom de/serialization functions for Rust's serde - feature "schemars_0_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(schemars-0.9) >= 0.9.0
Requires:       crate(serde-json-1) >= 1.0.145
Requires:       crate(serde-with-macros-3/schemars-0-9) >= 3.20.0
Provides:       crate(%{pkgname}/schemars-0-9) = %{version}

%description -n %{name}+schemars-0-9
This metapackage enables feature "schemars_0_9" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars-1
Summary:        Custom de/serialization functions for Rust's serde - feature "schemars_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(schemars-1) >= 1.0.2
Requires:       crate(serde-json-1) >= 1.0.145
Requires:       crate(serde-with-macros-3/schemars-1) >= 3.20.0
Provides:       crate(%{pkgname}/schemars-1) = %{version}

%description -n %{name}+schemars-1
This metapackage enables feature "schemars_1" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec-1
Summary:        Custom de/serialization functions for Rust's serde - feature "smallvec_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec-1) = %{version}

%description -n %{name}+smallvec-1
This metapackage enables feature "smallvec_1" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Custom de/serialization functions for Rust's serde - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bs58-0.5/std) >= 0.5.1
Requires:       crate(chrono-0.4/clock) >= 0.4.20
Requires:       crate(chrono-0.4/serde) >= 0.4.20
Requires:       crate(chrono-0.4/std) >= 0.4.20
Requires:       crate(indexmap-1/serde-1) >= 1.8.0
Requires:       crate(indexmap-1/std) >= 1.8.0
Requires:       crate(indexmap-2/serde) >= 2.0.0
Requires:       crate(indexmap-2/std) >= 2.0.0
Requires:       crate(schemars-0.9/std) >= 0.9.0
Requires:       crate(schemars-1/std) >= 1.0.2
Requires:       crate(serde-core-1/result) >= 1.0.225
Requires:       crate(serde-core-1/std) >= 1.0.225
Requires:       crate(time-0.3/serde-well-known) >= 0.3.47
Requires:       crate(time-0.3/std) >= 0.3.47
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time-0-3
Summary:        Custom de/serialization functions for Rust's serde - feature "time_0_3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.47
Provides:       crate(%{pkgname}/time-0-3) = %{version}

%description -n %{name}+time-0-3
This metapackage enables feature "time_0_3" for the Rust serde_with crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
