# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name allocative
%global full_version 0.3.6
%global pkgname allocative-0.3

Name:           rust-allocative-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "allocative"
License:        Apache-2.0
URL:            https://github.com/facebookexperimental/allocative
#!RemoteAsset:  sha256:d8cf9afc79c83d514444b55df3935d317da54b1ce3b17a133c646889cc260de8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(allocative-derive-0.3/default) >= 0.3.6
Requires:       crate(ctor-1/default) >= 1.0.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "allocative"

%package     -n %{name}+anyhow
Summary:        Inspect rust object tree and output it as flamegraph - feature "anyhow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anyhow-1/default) >= 1.0.65
Provides:       crate(%{pkgname}/anyhow) = %{version}

%description -n %{name}+anyhow
This metapackage enables feature "anyhow" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bumpalo
Summary:        Inspect rust object tree and output it as flamegraph - feature "bumpalo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bumpalo-3/default) >= 3.11.1
Provides:       crate(%{pkgname}/bumpalo) = %{version}

%description -n %{name}+bumpalo
This metapackage enables feature "bumpalo" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compact-str
Summary:        Inspect rust object tree and output it as flamegraph - feature "compact_str"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compact-str-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/compact-str) = %{version}

%description -n %{name}+compact-str
This metapackage enables feature "compact_str" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dashmap
Summary:        Inspect rust object tree and output it as flamegraph - feature "dashmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dashmap-6/default) >= 6.1.0
Provides:       crate(%{pkgname}/dashmap) = %{version}

%description -n %{name}+dashmap
This metapackage enables feature "dashmap" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either
Summary:        Inspect rust object tree and output it as flamegraph - feature "either"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/either) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Inspect rust object tree and output it as flamegraph - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.24
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Inspect rust object tree and output it as flamegraph - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.16/default) >= 0.16.1
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Inspect rust object tree and output it as flamegraph - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.2.6
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Inspect rust object tree and output it as flamegraph - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Inspect rust object tree and output it as flamegraph - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.21.4
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Inspect rust object tree and output it as flamegraph - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.11/default) >= 0.11.2
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost-types
Summary:        Inspect rust object tree and output it as flamegraph - feature "prost-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-types-0.14/default) >= 0.14.3
Provides:       crate(%{pkgname}/prost-types) = %{version}

%description -n %{name}+prost-types
This metapackage enables feature "prost-types" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Inspect rust object tree and output it as flamegraph - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.48
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Inspect rust object tree and output it as flamegraph - feature "slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slab-0.4/default) >= 0.4.12
Provides:       crate(%{pkgname}/slab) = %{version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Inspect rust object tree and output it as flamegraph - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sorted-vector-map
Summary:        Inspect rust object tree and output it as flamegraph - feature "sorted_vector_map"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sorted-vector-map-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/sorted-vector-map) = %{version}

%description -n %{name}+sorted-vector-map
This metapackage enables feature "sorted_vector_map" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Inspect rust object tree and output it as flamegraph - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.5.0
Requires:       crate(tokio-1/sync) >= 1.5.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+triomphe
Summary:        Inspect rust object tree and output it as flamegraph - feature "triomphe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(triomphe-0.1/default) >= 0.1.8
Provides:       crate(%{pkgname}/triomphe) = %{version}

%description -n %{name}+triomphe
This metapackage enables feature "triomphe" for the Rust allocative crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
