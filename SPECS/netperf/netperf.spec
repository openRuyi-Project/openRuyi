# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit       afc51ff9764741da4ed6702651fba9d9c23f8557
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           netperf
Version:        0+git20260202.%{shortcommit}
Release:        %autorelease
Summary:        Benchmark to measure the performance of many different types of networking
License:        MIT
URL:            https://github.com/HewlettPackard/netperf
#!RemoteAsset
Source0:        https://github.com/HewlettPackard/netperf/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-burst
BuildOption(conf):  --enable-dccp
BuildOption(conf):  --enable-demo
BuildOption(conf):  --enable-dirty
BuildOption(conf):  --enable-histogram
BuildOption(conf):  --enable-intervals
BuildOption(conf):  --enable-omni
BuildOption(conf):  --enable-sctp
BuildOption(conf):  --enable-unixdomain
BuildOption(build):  CFLAGS="%{optflags} -fno-strict-aliasing -fcommon -std=c99 -D_GNU_SOURCE"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  pkgconfig(libsctp)

%description
Netperf is a benchmark that can be used to measure the performance of many
different types of networking. It provides tests for both unidirectional
throughput, and end-to-end latency.

%package        help
Summary:        Help files for %{name}
BuildArch:      noarch

%description    help
Help files for %{name}.

%prep
%autosetup -n %{name}-%{commit}

%conf -p
autoreconf -fiv -I src/missing/m4

%install -a
rm -rf %{buildroot}%{_infodir}/dir

%files
%defattr(-,root,root,0755)
%doc README AUTHORS Release_Notes
%license COPYING
%{_bindir}/netperf
%{_bindir}/netserver
%{_infodir}/netperf.*

%files help
%doc doc/netperf.{html,pdf,txt,xml}
%doc doc/examples
%{_mandir}/man1/*

%changelog
%autochangelog
