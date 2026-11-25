# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow
%global full_version 57.3.1
%global pkgname arrow-57

Name:           rust-arrow-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:3bd47f2a6ddc39244bd722a27ee5da66c03369d087b9e024eafdb03e98b98ea7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-arith-57/default) >= 57.3.1
Requires:       crate(arrow-array-57/default) >= 57.3.1
Requires:       crate(arrow-buffer-57/default) >= 57.3.1
Requires:       crate(arrow-cast-57/default) >= 57.3.1
Requires:       crate(arrow-data-57/default) >= 57.3.1
Requires:       crate(arrow-ord-57/default) >= 57.3.1
Requires:       crate(arrow-row-57/default) >= 57.3.1
Requires:       crate(arrow-schema-57/default) >= 57.3.1
Requires:       crate(arrow-select-57/default) >= 57.3.1
Requires:       crate(arrow-string-57/default) >= 57.3.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "arrow"

%package     -n %{name}+arrow-csv
Summary:        Apache Arrow - feature "arrow-csv" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-csv-57/default) >= 57.3.1
Provides:       crate(%{pkgname}/arrow-csv) = %{version}
Provides:       crate(%{pkgname}/csv) = %{version}

%description -n %{name}+arrow-csv
This metapackage enables feature "arrow-csv" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "csv" feature.

%package     -n %{name}+arrow-ipc
Summary:        Apache Arrow - feature "arrow-ipc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-ipc-57/default) >= 57.3.1
Provides:       crate(%{pkgname}/arrow-ipc) = %{version}
Provides:       crate(%{pkgname}/ipc) = %{version}

%description -n %{name}+arrow-ipc
This metapackage enables feature "arrow-ipc" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ipc" feature.

%package     -n %{name}+arrow-json
Summary:        Apache Arrow - feature "arrow-json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-json-57/default) >= 57.3.1
Provides:       crate(%{pkgname}/arrow-json) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+arrow-json
This metapackage enables feature "arrow-json" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%package     -n %{name}+canonical-extension-types
Summary:        Apache Arrow - feature "canonical_extension_types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-schema-57/canonical-extension-types) >= 57.3.1
Provides:       crate(%{pkgname}/canonical-extension-types) = %{version}

%description -n %{name}+canonical-extension-types
This metapackage enables feature "canonical_extension_types" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-tz
Summary:        Apache Arrow - feature "chrono-tz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-array-57/chrono-tz) >= 57.3.1
Provides:       crate(%{pkgname}/chrono-tz) = %{version}

%description -n %{name}+chrono-tz
This metapackage enables feature "chrono-tz" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Apache Arrow - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/csv) = %{version}
Requires:       crate(%{pkgname}/ipc) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffi
Summary:        Apache Arrow - feature "ffi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-array-57/ffi) >= 57.3.1
Requires:       crate(arrow-data-57/ffi) >= 57.3.1
Requires:       crate(arrow-schema-57/ffi) >= 57.3.1
Provides:       crate(%{pkgname}/ffi) = %{version}

%description -n %{name}+ffi
This metapackage enables feature "ffi" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+force-validate
Summary:        Apache Arrow - feature "force_validate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-array-57/force-validate) >= 57.3.1
Requires:       crate(arrow-data-57/force-validate) >= 57.3.1
Provides:       crate(%{pkgname}/force-validate) = %{version}

%description -n %{name}+force-validate
This metapackage enables feature "force_validate" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipc-compression
Summary:        Apache Arrow - feature "ipc_compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ipc) = %{version}
Requires:       crate(arrow-ipc-57/lz4) >= 57.3.1
Requires:       crate(arrow-ipc-57/zstd) >= 57.3.1
Provides:       crate(%{pkgname}/ipc-compression) = %{version}

%description -n %{name}+ipc-compression
This metapackage enables feature "ipc_compression" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prettyprint
Summary:        Apache Arrow - feature "prettyprint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-cast-57/prettyprint) >= 57.3.1
Provides:       crate(%{pkgname}/prettyprint) = %{version}

%description -n %{name}+prettyprint
This metapackage enables feature "prettyprint" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pyarrow
Summary:        Apache Arrow - feature "pyarrow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ffi) = %{version}
Requires:       crate(arrow-pyarrow-57/default) >= 57.3.1
Provides:       crate(%{pkgname}/pyarrow) = %{version}

%description -n %{name}+pyarrow
This metapackage enables feature "pyarrow" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-utils
Summary:        Apache Arrow - feature "test_utils"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(rand-0.9/std) >= 0.9.0
Requires:       crate(rand-0.9/std-rng) >= 0.9.0
Requires:       crate(rand-0.9/thread-rng) >= 0.9.0
Provides:       crate(%{pkgname}/test-utils) = %{version}

%description -n %{name}+test-utils
This metapackage enables feature "test_utils" for the Rust arrow crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
