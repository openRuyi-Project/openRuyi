# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kmod
Version:        34.2
Release:        %autorelease
Summary:        Linux kernel module management utilities
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND FSFUL AND FSFULLRWD AND LGPL-2.1-only AND LGPL-2.1-or-later AND X11
URL:            https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git
#!RemoteAsset
Source0:        https://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --with-openssl
BuildOption(conf):  --with-zlib
BuildOption(conf):  --with-xz
BuildOption(conf):  --with-zstd
BuildOption(conf):  --enable-debug

BuildRequires:  chrpath
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  scdoc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libzstd)

Provides:       %{_sbindir}/modprobe

%description
The kmod package provides various programs needed for automatic
loading and unloading of modules under 2.6, 3.x, and later kernels, as well
as other module management programs. Device drivers and filesystems are two
examples of loaded and unloaded modules.

%package        libs
Summary:        Libraries to handle kernel module loading and unloading

%description    libs
The kmod-libs package provides runtime libraries for any application that
wishes to load or unload Linux kernel modules from the running system.

%package        devel
Summary:        Header files for kmod development
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The kmod-devel package provides header files used for development of
applications that wish to load or unload Linux kernel modules.

%conf -p
# We do not want to add gtk-doc
rm -f m4/gtk-doc.m4 libkmod/docs/gtk-doc.make
touch m4/gtk-doc.m4 libkmod/docs/gtk-doc.make
autoreconf --install

%install -a
pushd $RPM_BUILD_ROOT%{_mandir}/man5
ln -s modprobe.d.5.gz modprobe.conf.5.gz
popd

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/depmod.d
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d

%check

%files
%dir %{_sysconfdir}/depmod.d
%dir %{_sysconfdir}/modprobe.d
%dir %{_prefix}/lib/modprobe.d
%{_bindir}/kmod
%{_sbindir}/modprobe
%{_sbindir}/modinfo
%{_sbindir}/insmod
%{_sbindir}/rmmod
%{_sbindir}/lsmod
%{_sbindir}/depmod
%if %{with weak_modules}
%{_sbindir}/weak-modules
%endif
%{_datadir}/bash-completion/
%{_datadir}/fish/vendor_functions.d/*
%{_datadir}/zsh/site-functions/*
%if %{with dist_conf}
%{_sysconfdir}/depmod.d/dist.conf
%endif
%attr(0644,root,root) %{_mandir}/man5/mod*.d*.5*
%attr(0644,root,root) %{_mandir}/man5/depmod.d.5*
%{_mandir}/man5/modprobe.conf.5*
%attr(0644,root,root) %{_mandir}/man8/*.8*
%doc NEWS README.md

%files libs
%license COPYING
%{_libdir}/libkmod.so.*

%files devel
%{_includedir}/libkmod.h
%{_datadir}/pkgconfig/kmod.pc
%{_libdir}/pkgconfig/libkmod.pc
%{_libdir}/libkmod.so

%changelog
%{?autochangelog}
