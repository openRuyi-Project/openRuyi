# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bpftool
Version:        7.7.0
Release:        %autorelease
Summary:        Tool for inspection and manipulation of BPF programs and maps
License:        GPL-2.0-only OR BSD-2-Clause
URL:            https://github.com/libbpf/bpftool
#!RemoteAsset:  sha256:7d46a381f607432bdb5201a08b889924b6a4883bf09e8efca82a86a7d122cc97
Source0:        https://github.com/libbpf/bpftool/releases/download/v%{version}/bpftool-libbpf-v%{version}-sources.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -p1 -n bpftool-libbpf-v%{version}-sources
BuildOption(build):  -C src
BuildOption(build):  EXTRA_CFLAGS="%{optflags}"
BuildOption(build):  EXTRA_LDFLAGS="%{?build_ldflags}"
BuildOption(install):  -C src
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  bash_compdir=%{bash_completions_dir}
BuildOption(install):  mandir=%{_mandir}
BuildOption(install):  doc-install

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  binutils-devel
BuildRequires:  clang
BuildRequires:  python3-docutils
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libssl)

%description
bpftool allows for inspection and simple modification of BPF objects (programs
and maps) on the system.

# No configure
%conf

%build -a
%make_build -C docs V=1 man prefix=%{_prefix} mandir=%{_mandir}

%install -a
# bpftool Makefile hardcodes installation to %%{_prefix}/sbin
mv %{buildroot}%{_prefix}/sbin %{buildroot}%{_bindir}

# No tests
%check

%files
%license LICENSE LICENSE.BSD-2-Clause LICENSE.GPL-2.0
%doc README.md CHECKPOINT-COMMIT BPF-CHECKPOINT-COMMIT
%{_sbindir}/bpftool
%{bash_completions_dir}/bpftool
%{_mandir}/man8/bpftool*.8*

%changelog
%autochangelog
