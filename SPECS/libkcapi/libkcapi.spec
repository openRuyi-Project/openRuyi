# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond systemd 1

Name:           libkcapi
Version:        1.5.0
Release:        %autorelease
Summary:        Linux Kernel Crypto API User Space Interface Library
License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://www.chronox.de/libkcapi/
VCs:            git:https://github.com/smuellerDD/libkcapi
#!RemoteAsset
Source0:        https://www.chronox.de/libkcapi/releases/%{version}/libkcapi-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --enable-kcapi-encapp
BuildOption(conf):  --enable-kcapi-dgstapp
BuildOption(conf):  --enable-kcapi-hasher
BuildOption(conf):  --enable-kcapi-rngapp
BuildOption(conf):  --enable-kcapi-speed
BuildOption(conf):  --enable-kcapi-test
BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-sum-prefix=
BuildOption(conf):  --enable-sum-dir=%{_libdir}
BuildOption(conf):  --with-pkgconfigdir=%{_libdir}/pkgconfig

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  hardlink
BuildRequires:  libtool
BuildRequires:  openssl
BuildRequires:  perl
BuildRequires:  linux-headers >= 4.10.0
%if %{with systemd}
BuildRequires:  systemd

Requires:       systemd
%endif

%description
The Linux kernel exports a Netlink interface to allow user space to utilize
the kernel crypto API. libkcapi uses this interface and provides an easy to use
API for developers.

%package        devel
Summary:        Development files for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and development libraries for applications that use %{name}.

%prep -a
%if %{with systemd}
cat << EOF > 50-%{name}-optmem_max.conf
net.core.optmem_max = 81920
EOF
cat << EOF > README.preset
This package increases the kernel socket ancillary buffer size to 81920 bytes
via a sysctl.d preset file to improve performance for the Kernel Crypto API.
EOF
%endif

%conf -p
autoreconf -fiv

%install -a
%if %{with systemd}
install -D -m 0644 -t %{buildroot}%{_sysctldir} 50-%{name}-optmem_max.conf
%endif

install -d -m 755 %{buildroot}%{_docdir}/%{name}
%if %{with systemd}
install -m 0644 README.preset %{buildroot}%{_docdir}/%{name}/
%endif

# create symbolic link to /usr/bin/
for app in sha1hmac sha224hmac sha256hmac sha384hmac sha512hmac sm3hmac fipscheck fipshmac; do
    ln -s ../libexec/%{name}/$app %{buildroot}%{_bindir}/$app
done

%files
%license COPYING*
%doc %{_docdir}/%{name}
%if %{with systemd}
%{_sysctldir}/50-libkcapi-optmem_max.conf
%endif
%{_libdir}/libkcapi.so.*
%dir %{_libdir}/hmaccalc
%{_libdir}/hmaccalc/*.hmac
%{_bindir}/*
%{_libexecdir}/libkcapi
%{_mandir}/man*/*

%files          devel
%{_includedir}/kcapi.h
%{_libdir}/libkcapi.so
%{_libdir}/pkgconfig/libkcapi.pc

%changelog
%autochangelog
