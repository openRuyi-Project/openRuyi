# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bpftrace
Version:        0.26.1
Release:        %autorelease
Summary:        High-level tracing language for Linux eBPF
License:        Apache-2.0
URL:            https://github.com/iovisor/bpftrace
#!RemoteAsset:  sha256:555368f32f94bfcb74b119a3d9c67b68200be6375b8f452f794a2d3f6ebbcd16
Source0:        https://github.com/bpftrace/bpftrace/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING:BOOL=ON
BuildOption(conf):  -DBUILD_SHARED_LIBS:BOOL=OFF
BuildOption(conf):  -DUSE_SYSTEM_LIBBPF=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
BuildRequires:  bcc-devel >= 0.19.0-1
BuildRequires:  libbpf-devel
BuildRequires:  libiberty-devel
BuildRequires:  libbpf-static
BuildRequires:  binutils-devel
BuildRequires:  xxd
BuildRequires:  zip
BuildRequires:  cereal-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  bpftool
BuildRequires:  dwarves
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)

%description
BPFtrace is a high-level tracing language for Linux enhanced Berkeley Packet
Filter (eBPF) available in recent Linux kernels (4.x). BPFtrace uses LLVM as a
backend to compile scripts to BPF-bytecode and makes use of BCC for interacting
with the Linux BPF system, as well as existing Linux tracing capabilities:
kernel dynamic tracing (kprobes), user-level dynamic tracing (uprobes), and
tracepoints. The BPFtrace language is inspired by awk and C, and predecessor
tracers such as DTrace and SystemTap.

%check
GTEST_FILTER='-attachpoint_checker.rawtracepoint:TypeCheckerTest.array_in_map:TypeCheckerTest.array_compare:TypeCheckerTest.intarray_to_int_cast:TypeCheckerTest.type_ctx:TypeCheckerTest.for_loop_no_ctx_access' \
ctest --output-on-failure

%files
%doc README.md
%doc docs/language.md docs/reference_guide.md docs/stdlib.md docs/tutorial_one_liners.md
%dir %{_datadir}/bpftrace
%dir %{_datadir}/bpftrace/tools
%dir %{_datadir}/bpftrace/tools/old
%license LICENSE
%{_bindir}/bpftrace
%{_bindir}/bpftrace-aotrt
%{_mandir}/man8/*
%attr(0755,-,-) %{_datadir}/%{name}/tools/*.bt
%attr(0755,-,-) %{_datadir}/%{name}/tools/old/*.bt
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
