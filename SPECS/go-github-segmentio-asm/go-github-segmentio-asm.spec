# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           asm
%define go_import_path  github.com/segmentio/asm

Name:           go-github-segmentio-asm
Version:        1.2.1
Release:        %autorelease
Summary:        Go library providing algorithms that use modern CPU features
License:        MIT-0
URL:            https://github.com/segmentio/asm
#!RemoteAsset:  sha256:47bd144ee60642b19a0118143005038e4ce5009f8e90e3ec168a257099ac887d
Source0:        https://github.com/segmentio/asm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n asm-1.2.1
# build/* packages are generator helpers and fail with the current cpu feature API;
# runtime packages such as base64/keyset are still tested.
%define go_test_exclude_glob github.com/segmentio/asm/build*

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mmcloughlin/avo/build)
BuildRequires:  go(github.com/mmcloughlin/avo/gotypes)
BuildRequires:  go(github.com/mmcloughlin/avo/operand)
BuildRequires:  go(github.com/mmcloughlin/avo/reg)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/cpu)
BuildRequires:  go(golang.org/x/sys/unix)

Provides:       go(github.com/segmentio/asm) = %{version}
Provides:       go(github.com/segmentio/asm/ascii) = %{version}
Provides:       go(github.com/segmentio/asm/base64) = %{version}
Provides:       go(github.com/segmentio/asm/bswap) = %{version}
Provides:       go(github.com/segmentio/asm/cpu) = %{version}
Provides:       go(github.com/segmentio/asm/cpu/arm) = %{version}
Provides:       go(github.com/segmentio/asm/cpu/arm64) = %{version}
Provides:       go(github.com/segmentio/asm/cpu/cpuid) = %{version}
Provides:       go(github.com/segmentio/asm/cpu/x86) = %{version}
Provides:       go(github.com/segmentio/asm/internal) = %{version}
Provides:       go(github.com/segmentio/asm/internal/buffer) = %{version}
Provides:       go(github.com/segmentio/asm/internal/unsafebytes) = %{version}
Provides:       go(github.com/segmentio/asm/keyset) = %{version}
Provides:       go(github.com/segmentio/asm/mem) = %{version}
Provides:       go(github.com/segmentio/asm/qsort) = %{version}
Provides:       go(github.com/segmentio/asm/slices) = %{version}
Provides:       go(github.com/segmentio/asm/sortedset) = %{version}
Provides:       go(github.com/segmentio/asm/utf8) = %{version}

Requires:       go(github.com/mmcloughlin/avo/build)
Requires:       go(github.com/mmcloughlin/avo/gotypes)
Requires:       go(github.com/mmcloughlin/avo/operand)
Requires:       go(github.com/mmcloughlin/avo/reg)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/cpu)
Requires:       go(golang.org/x/sys/unix)


%description
asm provides Go implementations of performance-sensitive algorithms optimized
to use modern CPU features and instruction sets.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
