# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name palette
%global full_version 0.7.6
%global pkgname palette-0.7

Name:           rust-palette-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "palette"
License:        MIT OR Apache-2.0
URL:            https://github.com/Ogeon/palette
#!RemoteAsset:  sha256:4cbf71184cc5ecc2e4e1baccdb21026c20e5fc3dcf63028a086131b3ab00b6e6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fast-srgb8-1/default) >= 1.0.0
Requires:       crate(palette-derive-0.7/default) >= 0.7.6
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/named) = %{version}

%description
Source code for takopackized Rust crate "palette"

%package     -n %{name}+approx
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "approx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(approx-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/approx) = %{version}

%description -n %{name}+approx
This metapackage enables feature "approx" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/approx) = %{version}
Requires:       crate(%{pkgname}/named-from-str) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+find-crate
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "find-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(palette-derive-0.7/find-crate) >= 0.7.6
Provides:       crate(%{pkgname}/find-crate) = %{version}

%description -n %{name}+find-crate
This metapackage enables feature "find-crate" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libm-0.2) >= 0.2.1
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+named-from-str
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "named_from_str"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/named) = %{version}
Requires:       crate(%{pkgname}/phf) = %{version}
Provides:       crate(%{pkgname}/named-from-str) = %{version}

%description -n %{name}+named-from-str
This metapackage enables feature "named_from_str" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "phf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.11/macros) >= 0.11.0
Provides:       crate(%{pkgname}/phf) = %{version}

%description -n %{name}+phf
This metapackage enables feature "phf" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "rand" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "random" feature.

%package     -n %{name}+serde
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/serde-derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serializing
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "serializing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/serializing) = %{version}

%description -n %{name}+serializing
This metapackage enables feature "serializing" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(approx-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wide
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "wide"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wide-0.7) >= 0.7.3
Provides:       crate(%{pkgname}/wide) = %{version}

%description -n %{name}+wide
This metapackage enables feature "wide" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
