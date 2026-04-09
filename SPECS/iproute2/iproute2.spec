# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iproute2
Version:        6.16.0
Release:        %autorelease
Summary:        Advanced IP routing and network device configuration tools
License:        BSD-4-Clause-UC AND GPL-2.0-or-later
URL:            https://wiki.linuxfoundation.org/networking/iproute2
VCS:            git:https://git.kernel.org/pub/scm/network/iproute2/iproute2
#!RemoteAsset
Source0:        https://kernel.org/pub/linux/utils/net/iproute2/iproute2-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --color auto

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig(xtables)
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libselinux)

%description
The iproute2 package contains networking utilities (ip and rtmon, for example)
which are designed to use the advanced networking capabilities of the Linux
kernel.

%package        devel
Summary:        iproute2 development files
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libnetlink static library.

%build -p
echo -e "\nPREFIX=%{_prefix}\nSBINDIR=%{_sbindir}" >> config.mk

%install -a
echo '.so man8/tc-cbq.8' > %{buildroot}%{_mandir}/man8/cbq.8

# For libnetlink
install -D -m644 include/libnetlink.h %{buildroot}%{_includedir}/libnetlink.h
install -D -m644 lib/libnetlink.a %{buildroot}%{_libdir}/libnetlink.a

# No docs
rm -rf %{buildroot}%{_docdir}

# There is a test suite, but it wants network namespaces and sudo.
%check

%files
%license COPYING
%dir %{_datadir}/iproute2
%doc README README.devel
%{_mandir}/man7/*
%{_mandir}/man8/*
%attr(644,root,root) %config %{_datadir}/iproute2/*
%{_sbindir}/*
%{_libdir}/tc/*
%{_datadir}/bash-completion/completions/devlink
%{_datadir}/bash-completion/completions/tc

%files devel
%license COPYING
%{_mandir}/man3/*
%{_libdir}/libnetlink.a
%{_includedir}/libnetlink.h
%{_includedir}/iproute2/bpf_elf.h

%changelog
%autochangelog
