# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iperf
Version:        3.20
Release:        %autorelease
Summary:        A TCP, UDP, and SCTP network bandwidth measurement tool
License:        BSD-3-Clause
URL:            https://software.es.net/iperf/
VCS:            git:https://github.com/esnet/iperf
#!RemoteAsset
Source0:        https://github.com/esnet/iperf/archive/%{version}/iperf-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  util-linux-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  make

%description
iperf is a tool for active measurements of the maximum achievable bandwidth
on IP networks. It supports tuning of various parameters related to timing,
protocols, and buffers. For each test it reports the measured throughput/bitrate,
loss, and other parameters.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -a
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%install
%make_install -C src INSTALL_DIR="%{buildroot}%{_bindir}"
mkdir -p %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_libdir}/libiperf.la

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md RELNOTES.md
%{_bindir}/iperf3
%{_libdir}/*.so.*
%{_mandir}/man1/iperf3.1.gz
%{_mandir}/man3/libiperf.3.gz

%files devel
%defattr(-,root,root)
%{_includedir}/iperf_api.h
%{_libdir}/*.so

%changelog
%autochangelog
