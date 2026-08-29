# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# pkgconf acts as pkgconfig
%bcond_without pkgconfig_compat

%if %{with pkgconfig_compat}
%global pkgconfig_ver 0.29.2
# For obsoleting pkgconfig, bump the ver to a number higher than latest version
%global pkgconfig_obsver %{pkgconfig_ver}+1
%endif

# pkgconfig platform
%global pkgconf_target_platform %{_target_platform}%{?_gnu}

# Search path for pc files for pkgconf
%global pkgconf_libdirs %{_libdir}/pkgconfig:%{_datadir}/pkgconfig

%global somajor 7
%global libname lib%{name}%{somajor}
%global devname lib%{name}-devel

Name:           pkgconf
Version:        2.5.1
Release:        %autorelease
Summary:        Package compiler and linker metadata toolkit
License:        ISC
URL:            https://pkgconf.org/
VCS:            git:https://github.com/pkgconf/pkgconf.git
#!RemoteAsset:  sha256:cd05c9589b9f86ecf044c10a2269822bc9eb001eced2582cfffd658b0a50c243
Source0:        https://distfiles.dereferenced.org/%{name}/%{name}-%{version}.tar.xz
# Simple wrapper script to offer platform versions of pkgconfig from Fedora
Source1:        platform-pkg-config.in
Buildsystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-pkg-config-dir=%{pkgconf_libdirs}
BuildOption(conf):  --with-system-includedir=%{_includedir}
BuildOption(conf):  --with-system-libdir=%{_libdir}

BuildRequires:  gcc
BuildRequires:  make
# for tests.
BuildRequires:  kyua
BuildRequires:  atf

# pkgconf uses libpkgconf internally
Requires:       %{libname}%{?_isa} = %{version}-%{release}

# This is defined within pkgconf code as a virtual pc (just like in pkgconfig)
Provides:       pkgconfig(pkgconf) = %{version}

%description
pkgconf is a program which helps to configure compiler and linker flags
for development frameworks. It is similar to pkg-config from freedesktop.org
and handles .pc files in a similar manner as pkg-config.

%package     -n %{libname}
Summary:        Backend library for %{name}
License:        ISC

%description -n %{libname}
This package provides libraries for applications to use the functionality
of %{name}.

%package     -n %{devname}
Summary:        Development files for lib%{name}
License:        ISC
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# Avoid dependency loop on itself by specifying the Provides directly
Provides:       pkgconfig(libpkgconf) = %{version}

%description -n %{devname}
This package provides files necessary for developing applications
to use functionality provided by %{name}.

%if %{with pkgconfig_compat}
%package        m4
Summary:        m4 macros for pkgconf
License:        GPL-2.0-or-later WITH Autoconf-exception-2.0
BuildArch:      noarch
# Ensure that it Conflicts and Obsoletes pkgconfig since it contains content formerly from it
Conflicts:      pkgconfig < %{pkgconfig_obsver}
Obsoletes:      pkgconfig < %{pkgconfig_obsver}

%description    m4
This package includes m4 macros used to support PKG_CHECK_MODULES
when using pkgconf with autotools.

%package        pkg-config
Summary:        %{name} shim to provide /usr/bin/pkg-config
# Ensure that it Conflicts with pkg-config and is considered "better"
License:        ISC
Conflicts:      pkg-config < %{pkgconfig_obsver}
Obsoletes:      pkg-config < %{pkgconfig_obsver}
Provides:       pkg-config = %{pkgconfig_obsver}
Provides:       pkg-config%{?_isa} = %{pkgconfig_obsver}
# This is in the original pkgconfig package, set to match output from pkgconf
Provides:       pkgconfig(pkg-config) = %{version}
# Fedora/Mageia pkgconfig Provides for those who might use alternate package name
Provides:       pkgconfig = %{pkgconfig_obsver}
Provides:       pkgconfig%{?_isa} = %{pkgconfig_obsver}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-m4 = %{version}-%{release}

%description    pkg-config
This package provides the shim links for pkgconf to be automatically
used in place of pkgconfig. This ensures that pkgconf is used as
the system provider of pkg-config.
%endif

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/pkgconfig/personality.d
mkdir -p %{buildroot}%{_datadir}/pkgconfig/personality.d

# pkgconf rpm macros
mkdir -p %{buildroot}%{_rpmmacrodir}/

cat > %{buildroot}%{_rpmmacrodir}/macros.pkgconf <<EOM
%%pkgconfig_personalitydir %{_datadir}/pkgconfig/personality.d
EOM

# Purge autotools-created docdir, as we'll docify later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%if %{with pkgconfig_compat}
install -pm 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{pkgconf_target_platform}-pkg-config

sed -e "s|@TARGET_PLATFORM@|%{pkgconf_target_platform}|" \
    -e "s|@PKGCONF_LIBDIRS_LOCAL@|/usr/local/%{_lib}/pkgconfig:/usr/local/share/pkgconfig:%{pkgconf_libdirs}|" \
    -e "s|@PKGCONF_SYSLIBDIR_LOCAL@|/usr/local/%{_lib}:%{_libdir}|" \
    -e "s|@PKGCONF_SYSINCDIR_LOCAL@|/usr/local/include:%{_includedir}|" \
    -e "s|@PKGCONF_LIBDIRS@|%{pkgconf_libdirs}|" \
    -e "s|@PKGCONF_SYSLIBDIR@|%{_libdir}|" \
    -e "s|@PKGCONF_SYSINCDIR@|%{_includedir}|" \
    -i %{buildroot}%{_bindir}/%{pkgconf_target_platform}-pkg-config

ln -sr %{buildroot}%{_bindir}/%{pkgconf_target_platform}-pkg-config %{buildroot}%{_bindir}/pkg-config

# Link pkg-config(1) to pkgconf(1)
echo ".so man1/pkgconf.1" > %{buildroot}%{_mandir}/man1/pkg-config.1

mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_datadir}/pkgconfig
%endif

# If we're not providing pkgconfig override & compat
# we should not provide the pkgconfig m4 macros
%if ! %{with pkgconfig_compat}
rm -rf %{buildroot}%{_datadir}/aclocal
rm -rf %{buildroot}%{_mandir}/man7
%endif

%files
%license COPYING
%doc README.md AUTHORS NEWS
%{_bindir}/pkgconf
%{_bindir}/bomtool
%{_mandir}/man1/pkgconf.1*
%{_mandir}/man1/bomtool.1*
%{_mandir}/man5/pc.5*
%{_mandir}/man5/pkgconf-personality.5*
%{_rpmmacrodir}/macros.pkgconf
%dir %{_libdir}/pkgconfig
%dir %{_datadir}/pkgconfig
%dir %{_sysconfdir}/pkgconfig
%dir %{_sysconfdir}/pkgconfig/personality.d
%dir %{_datadir}/pkgconfig/personality.d

%files -n %{libname}
%license COPYING
%{_libdir}/libpkgconf*.so.%{somajor}
%{_libdir}/libpkgconf*.so.%{somajor}.*

%files -n %{devname}
%license COPYING
%{_libdir}/libpkgconf*.so
%{_includedir}/pkgconf/
%{_libdir}/pkgconfig/libpkgconf.pc

%if %{with pkgconfig_compat}
%files m4
%license COPYING
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/pkg.m4
%{_mandir}/man7/pkg.m4.7%{?ext_man}

%files pkg-config
%license COPYING
%{_bindir}/pkg-config
%{_bindir}/%{pkgconf_target_platform}-pkg-config
%{_mandir}/man1/pkg-config.1%{?ext_man}
%endif

%changelog
%autochangelog
