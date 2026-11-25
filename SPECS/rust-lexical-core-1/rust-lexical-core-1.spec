# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-core
%global full_version 1.0.6
%global pkgname lexical-core-1

Name:           rust-lexical-core-1
Version:        1.0.6
Release:        %autorelease
Summary:        Rust crate "lexical-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:7d8d125a277f807e55a77304455eb7b1cb52f2b18c143b60e766c120bd64a594
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lexical-util-1) >= 1.0.7

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lexical-core"

%package     -n %{name}+compact
Summary:        Lexical, to- and from-string conversion routines - feature "compact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1/compact) >= 1.0.6
Requires:       crate(lexical-parse-integer-1/compact) >= 1.0.6
Requires:       crate(lexical-write-float-1/compact) >= 1.0.6
Requires:       crate(lexical-write-integer-1/compact) >= 1.0.6
Provides:       crate(%{pkgname}/compact) = %{version}

%description -n %{name}+compact
This metapackage enables feature "compact" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Lexical, to- and from-string conversion routines - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parse-floats) = %{version}
Requires:       crate(%{pkgname}/parse-integers) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/write-floats) = %{version}
Requires:       crate(%{pkgname}/write-integers) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f128
Summary:        Lexical, to- and from-string conversion routines - feature "f128"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1/f128) >= 1.0.6
Requires:       crate(lexical-util-1/f128) >= 1.0.7
Requires:       crate(lexical-write-float-1/f128) >= 1.0.6
Provides:       crate(%{pkgname}/f128) = %{version}

%description -n %{name}+f128
This metapackage enables feature "f128" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f16
Summary:        Lexical, to- and from-string conversion routines - feature "f16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1/f16) >= 1.0.6
Requires:       crate(lexical-util-1/f16) >= 1.0.7
Requires:       crate(lexical-write-float-1/f16) >= 1.0.6
Provides:       crate(%{pkgname}/f16) = %{version}

%description -n %{name}+f16
This metapackage enables feature "f16" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+floats
Summary:        Lexical, to- and from-string conversion routines - feature "floats"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parse-floats) = %{version}
Requires:       crate(%{pkgname}/write-floats) = %{version}
Provides:       crate(%{pkgname}/floats) = %{version}

%description -n %{name}+floats
This metapackage enables feature "floats" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+format
Summary:        Lexical, to- and from-string conversion routines - feature "format"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1/format) >= 1.0.6
Requires:       crate(lexical-parse-integer-1/format) >= 1.0.6
Requires:       crate(lexical-util-1/format) >= 1.0.7
Requires:       crate(lexical-write-float-1/format) >= 1.0.6
Requires:       crate(lexical-write-integer-1/format) >= 1.0.6
Provides:       crate(%{pkgname}/format) = %{version}

%description -n %{name}+format
This metapackage enables feature "format" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+integers
Summary:        Lexical, to- and from-string conversion routines - feature "integers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parse-integers) = %{version}
Requires:       crate(%{pkgname}/write-integers) = %{version}
Provides:       crate(%{pkgname}/integers) = %{version}

%description -n %{name}+integers
This metapackage enables feature "integers" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lexical-parse-float
Summary:        Lexical, to- and from-string conversion routines - feature "lexical-parse-float" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1) >= 1.0.6
Provides:       crate(%{pkgname}/lexical-parse-float) = %{version}
Provides:       crate(%{pkgname}/parse-floats) = %{version}

%description -n %{name}+lexical-parse-float
This metapackage enables feature "lexical-parse-float" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "parse-floats" feature.

%package     -n %{name}+lexical-parse-integer
Summary:        Lexical, to- and from-string conversion routines - feature "lexical-parse-integer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-1) >= 1.0.6
Provides:       crate(%{pkgname}/lexical-parse-integer) = %{version}
Provides:       crate(%{pkgname}/parse-integers) = %{version}

%description -n %{name}+lexical-parse-integer
This metapackage enables feature "lexical-parse-integer" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "parse-integers" feature.

%package     -n %{name}+lexical-write-float
Summary:        Lexical, to- and from-string conversion routines - feature "lexical-write-float" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-write-float-1) >= 1.0.6
Provides:       crate(%{pkgname}/lexical-write-float) = %{version}
Provides:       crate(%{pkgname}/write-floats) = %{version}

%description -n %{name}+lexical-write-float
This metapackage enables feature "lexical-write-float" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "write-floats" feature.

%package     -n %{name}+lexical-write-integer
Summary:        Lexical, to- and from-string conversion routines - feature "lexical-write-integer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-write-integer-1) >= 1.0.6
Provides:       crate(%{pkgname}/lexical-write-integer) = %{version}
Provides:       crate(%{pkgname}/write-integers) = %{version}

%description -n %{name}+lexical-write-integer
This metapackage enables feature "lexical-write-integer" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "write-integers" feature.

%package     -n %{name}+lint
Summary:        Lexical, to- and from-string conversion routines - feature "lint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1/lint) >= 1.0.6
Requires:       crate(lexical-parse-integer-1/lint) >= 1.0.6
Requires:       crate(lexical-util-1/lint) >= 1.0.7
Requires:       crate(lexical-write-float-1/lint) >= 1.0.6
Requires:       crate(lexical-write-integer-1/lint) >= 1.0.6
Provides:       crate(%{pkgname}/lint) = %{version}

%description -n %{name}+lint
This metapackage enables feature "lint" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parse
Summary:        Lexical, to- and from-string conversion routines - feature "parse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parse-floats) = %{version}
Requires:       crate(%{pkgname}/parse-integers) = %{version}
Provides:       crate(%{pkgname}/parse) = %{version}

%description -n %{name}+parse
This metapackage enables feature "parse" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+power-of-two
Summary:        Lexical, to- and from-string conversion routines - feature "power-of-two"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1/power-of-two) >= 1.0.6
Requires:       crate(lexical-parse-integer-1/power-of-two) >= 1.0.6
Requires:       crate(lexical-util-1/power-of-two) >= 1.0.7
Requires:       crate(lexical-write-float-1/power-of-two) >= 1.0.6
Requires:       crate(lexical-write-integer-1/power-of-two) >= 1.0.6
Provides:       crate(%{pkgname}/power-of-two) = %{version}

%description -n %{name}+power-of-two
This metapackage enables feature "power-of-two" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+radix
Summary:        Lexical, to- and from-string conversion routines - feature "radix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/power-of-two) = %{version}
Requires:       crate(lexical-parse-float-1/radix) >= 1.0.6
Requires:       crate(lexical-parse-integer-1/radix) >= 1.0.6
Requires:       crate(lexical-util-1/radix) >= 1.0.7
Requires:       crate(lexical-write-float-1/radix) >= 1.0.6
Requires:       crate(lexical-write-integer-1/radix) >= 1.0.6
Provides:       crate(%{pkgname}/radix) = %{version}

%description -n %{name}+radix
This metapackage enables feature "radix" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Lexical, to- and from-string conversion routines - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-float-1/std) >= 1.0.6
Requires:       crate(lexical-parse-integer-1/std) >= 1.0.6
Requires:       crate(lexical-util-1/std) >= 1.0.7
Requires:       crate(lexical-write-float-1/std) >= 1.0.6
Requires:       crate(lexical-write-integer-1/std) >= 1.0.6
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write
Summary:        Lexical, to- and from-string conversion routines - feature "write"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/write-floats) = %{version}
Requires:       crate(%{pkgname}/write-integers) = %{version}
Provides:       crate(%{pkgname}/write) = %{version}

%description -n %{name}+write
This metapackage enables feature "write" for the Rust lexical-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
