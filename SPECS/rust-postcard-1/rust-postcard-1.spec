# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name postcard
%global full_version 1.1.3
%global pkgname postcard-1

Name:           rust-postcard-1
Version:        1.1.3
Release:        %autorelease
Summary:        Rust crate "postcard"
License:        MIT OR Apache-2.0
URL:            https://github.com/jamesmunns/postcard
#!RemoteAsset:  sha256:6764c3b5dd454e283a30e6dfe78e9b31096d9e32036b5d1eaac7a6119ccb9a24
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cobs-0.3) >= 0.3.0
Requires:       crate(serde-1/derive) >= 1.0.100
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core-num-saturating) = %{version}
Provides:       crate(%{pkgname}/paste) = %{version}

%description
Source code for takopackized Rust crate "postcard"

%package     -n %{name}+alloc
Summary:        No_std + serde compatible message library for Rust - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embedded-io-0.4/alloc) >= 0.4.0
Requires:       crate(embedded-io-0.6/alloc) >= 0.6.0
Requires:       crate(serde-1/alloc) >= 1.0.100
Requires:       crate(serde-1/derive) >= 1.0.100
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crc
Summary:        No_std + serde compatible message library for Rust - feature "crc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc-3/default) >= 3.0.1
Provides:       crate(%{pkgname}/crc) = %{version}
Provides:       crate(%{pkgname}/use-crc) = %{version}

%description -n %{name}+crc
This metapackage enables feature "crc" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use-crc" feature.

%package     -n %{name}+defmt
Summary:        No_std + serde compatible message library for Rust - feature "defmt" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/defmt) = %{version}
Provides:       crate(%{pkgname}/use-defmt) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use-defmt" feature.

%package     -n %{name}+embedded-io
Summary:        No_std + serde compatible message library for Rust - feature "embedded-io" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embedded-io-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/embedded-io) = %{version}
Provides:       crate(%{pkgname}/embedded-io-04) = %{version}

%description -n %{name}+embedded-io
This metapackage enables feature "embedded-io" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "embedded-io-04" feature.

%package     -n %{name}+embedded-io-06
Summary:        No_std + serde compatible message library for Rust - feature "embedded-io-06"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embedded-io-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/embedded-io-06) = %{version}

%description -n %{name}+embedded-io-06
This metapackage enables feature "embedded-io-06" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless
Summary:        No_std + serde compatible message library for Rust - feature "heapless"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heapless-0.7/serde) >= 0.7.0
Provides:       crate(%{pkgname}/heapless) = %{version}

%description -n %{name}+heapless
This metapackage enables feature "heapless" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless-cas
Summary:        No_std + serde compatible message library for Rust - feature "heapless-cas" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/heapless) = %{version}
Requires:       crate(heapless-0.7/cas) >= 0.7.0
Requires:       crate(heapless-0.7/serde) >= 0.7.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/heapless-cas) = %{version}

%description -n %{name}+heapless-cas
This metapackage enables feature "heapless-cas" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+nalgebra-v0-33
Summary:        No_std + serde compatible message library for Rust - feature "nalgebra_v0_33" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nalgebra-0.33) >= 0.33.0
Provides:       crate(%{pkgname}/nalgebra-v0-33) = %{version}

%description -n %{name}+nalgebra-v0-33
This metapackage enables feature "nalgebra_v0_33" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nalgebra-v0_33" feature.

%package     -n %{name}+postcard-derive
Summary:        No_std + serde compatible message library for Rust - feature "postcard-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(postcard-derive-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/experimental-derive) = %{version}
Provides:       crate(%{pkgname}/postcard-derive) = %{version}

%description -n %{name}+postcard-derive
This metapackage enables feature "postcard-derive" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "experimental-derive" feature.

%package     -n %{name}+use-std
Summary:        No_std + serde compatible message library for Rust - feature "use-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.100
Requires:       crate(serde-1/std) >= 1.0.100
Provides:       crate(%{pkgname}/use-std) = %{version}

%description -n %{name}+use-std
This metapackage enables feature "use-std" for the Rust postcard crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
