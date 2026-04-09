# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name            byte-unixbench
%define unixbench_prefix /opt/unixbench

Name:           unixbench
Version:        6.0.0
Release:        %autorelease
Summary:        The BYTE UNIX Benchmark
License:        GPL-2.0-only
URL:            https://code.google.com/archive/p/byte-unixbench/
VCS:            git:https://github.com/kdlucas/byte-unixbench
#!RemoteAsset
Source0:        https://github.com/kdlucas/byte-unixbench/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):   -n %{_name}-%{version} -p1
BuildOption(build):  all
BuildOption(build):  CC='gcc -std=gnu99'

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
UnixBench is the original BYTE UNIX benchmark suite.
The purpose of UnixBench is to provide a basic indicator of the performance
of a Unix-like system; hence, multiple tests are used to test various aspects
of the system's performance. These test results are then compared to the
scores from a baseline system to produce an index value, which is generally
easier to handle than the raw scores. The entire set of index values is then
combined to make an overall index for the system.

%conf
# No configure.

%build -p
cd UnixBench
# Switch to RVA23 profile
sed -i 's/rv64g/rva23u64/g' Makefile

# Skip automatic compilation check to use pre-built binaries
sed -i 's/^\([[:space:]]*\)preChecks();/\1# preChecks();/' Run

%install
# Use our own install step
cd UnixBench
mkdir -p %{buildroot}%{unixbench_prefix}/pgms
mkdir -p %{buildroot}%{unixbench_prefix}/testdir

install -m 0644 testdir/* %{buildroot}%{unixbench_prefix}/testdir
install -m 0644 README %{buildroot}%{unixbench_prefix}
install -m 0644 USAGE %{buildroot}%{unixbench_prefix}
install -m 0644 WRITING_TESTS %{buildroot}%{unixbench_prefix}
install -m 0755 Run %{buildroot}%{unixbench_prefix}
cp -rp pgms/* %{buildroot}%{unixbench_prefix}/pgms/

# No tests
%check

%files
%license LICENSE.txt
%doc README.md
%{unixbench_prefix}

%changelog
%autochangelog
