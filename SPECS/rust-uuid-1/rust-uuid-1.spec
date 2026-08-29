# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uuid
%global full_version 1.23.2
%global pkgname uuid-1

Name:           rust-uuid-1
Version:        1.23.2
Release:        %autorelease
Summary:        Rust crate "uuid"
License:        Apache-2.0 OR MIT
URL:            https://github.com/uuid-rs/uuid
#!RemoteAsset:  sha256:d258b83ceec21034727ecee8c382cfa6c3e133699b0742c64571814fb420c9f7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/macro-diagnostics) = %{version}
Provides:       crate(%{pkgname}/v8) = %{version}

%description
Source code for takopackized Rust crate "uuid"

%package     -n %{name}+arbitrary
Summary:        Generate and parse UUIDs - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.1.3
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+atomic
Summary:        Generate and parse UUIDs - feature "atomic" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atomic-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/atomic) = %{version}
Provides:       crate(%{pkgname}/v1) = %{version}
Provides:       crate(%{pkgname}/v6) = %{version}

%description -n %{name}+atomic
This metapackage enables feature "atomic" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v1", and "v6" features.

%package     -n %{name}+borsh
Summary:        Generate and parse UUIDs - feature "borsh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borsh-1) >= 1.0.0
Requires:       crate(borsh-derive-1) >= 1.0.0
Provides:       crate(%{pkgname}/borsh) = %{version}

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Generate and parse UUIDs - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.22.0
Requires:       crate(bytemuck-1/derive) >= 1.22.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast-rng
Summary:        Generate and parse UUIDs - feature "fast-rng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rng) = %{version}
Requires:       crate(rand-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/fast-rng) = %{version}

%description -n %{name}+fast-rng
This metapackage enables feature "fast-rng" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js
Summary:        Generate and parse UUIDs - feature "js"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3) >= 0.3.0
Requires:       crate(wasm-bindgen-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/js) = %{version}

%description -n %{name}+js
This metapackage enables feature "js" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+md5
Summary:        Generate and parse UUIDs - feature "md5" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(md-5-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/md5) = %{version}
Provides:       crate(%{pkgname}/v3) = %{version}

%description -n %{name}+md5
This metapackage enables feature "md5" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v3" feature.

%package     -n %{name}+rng
Summary:        Generate and parse UUIDs - feature "rng" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/rng) = %{version}
Provides:       crate(%{pkgname}/v4) = %{version}
Provides:       crate(%{pkgname}/v7) = %{version}

%description -n %{name}+rng
This metapackage enables feature "rng" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v4", and "v7" features.

%package     -n %{name}+rng-getrandom
Summary:        Generate and parse UUIDs - feature "rng-getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rng) = %{version}
Requires:       crate(%{pkgname}/uuid-rng-internal-lib) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(uuid-rng-internal-1/getrandom) >= 1.23.2
Provides:       crate(%{pkgname}/rng-getrandom) = %{version}

%description -n %{name}+rng-getrandom
This metapackage enables feature "rng-getrandom" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rng-rand
Summary:        Generate and parse UUIDs - feature "rng-rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rng) = %{version}
Requires:       crate(%{pkgname}/uuid-rng-internal-lib) = %{version}
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(uuid-rng-internal-1/rand) >= 1.23.2
Provides:       crate(%{pkgname}/rng-rand) = %{version}

%description -n %{name}+rng-rand
This metapackage enables feature "rng-rand" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Generate and parse UUIDs - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.221
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Generate and parse UUIDs - feature "sha1" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-smol-1) >= 1.0.0
Provides:       crate(%{pkgname}/sha1) = %{version}
Provides:       crate(%{pkgname}/v5) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v5" feature.

%package     -n %{name}+slog
Summary:        Generate and parse UUIDs - feature "slog"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slog-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/slog) = %{version}

%description -n %{name}+slog
This metapackage enables feature "slog" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Generate and parse UUIDs - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/std) >= 0.3.0
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+uuid-rng-internal-lib
Summary:        Generate and parse UUIDs - feature "uuid-rng-internal-lib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-rng-internal-1/default) >= 1.23.2
Provides:       crate(%{pkgname}/uuid-rng-internal-lib) = %{version}

%description -n %{name}+uuid-rng-internal-lib
This metapackage enables feature "uuid-rng-internal-lib" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy
Summary:        Generate and parse UUIDs - feature "zerocopy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerocopy-0.8/default) >= 0.8.0
Requires:       crate(zerocopy-0.8/derive) >= 0.8.0
Provides:       crate(%{pkgname}/zerocopy) = %{version}

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust uuid crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
