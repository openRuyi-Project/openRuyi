# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openjade
Version:        1.3.2
Release:        %autorelease
Summary:        A DSSSL implementation
License:        LicenseRef-DMIT
URL:            http://openjade.sourceforge.net/
#!RemoteAsset
Source0:        http://download.sourceforge.net/openjade/openjade-%{version}.tar.gz
BuildSystem:    autotools

# Use Getopt:Std to prevent build failure
Patch0:         0001-openjade-getoptperl.patch
# Do not require OpenSP libosp.la file for build
Patch1:         0002-openjade-nola.patch
# Do not link against -lnsl
Patch2:         0003-openjade-1.3.1-nsl.patch
# Fix dependent libs for libogrove
Patch3:         0004-openjade-deplibs.patch
# Upstream bug tracker fix
Patch4:         0005-openjade-1.3.2-gcc46.patch
# Fix build with newer compilers
Patch5:         0006-openjade-configure-c99.patch

BuildRequires:  config
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  opensp-devel
BuildRequires:  perl
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Getopt::Std)

Requires:       sgml-common

%description
OpenJade is an implementation of the ISO/IEC 10179:1996 standard DSSSL
(Document Style Semantics and Specification Language). OpenJade is
based on James Clark's Jade implementation of DSSSL. OpenJade is a
command-line application and a set of components. The DSSSL engine
inputs an SGML or XML document and can output a variety of formats:
XML, RTF, TeX, MIF (FrameMaker), SGML, or XML.

%conf
cp -p %{_bindir}/config.guess config/
cp -p %{_bindir}/config.sub config/
# This shit is driving me nuts - 251
# DO NOT TOUCH: https://bugs.launchpad.net/ubuntu/+source/openjade/+bug/1869734
CXXFLAGS="-O0"
%configure --disable-static \
    --datadir=%{_datadir}/sgml/%{name}-%{version} \
    --enable-splibdir=%{_libdir}

%install -a
ln -s openjade %{buildroot}/%{_bindir}/jade

# Install jade/jade %%{buildroot}/%%{prefix}/bin/jade
cp dsssl/catalog %{buildroot}/%{_datadir}/sgml/%{name}-%{version}/
cp dsssl/{dsssl,style-sheet,fot}.dtd %{buildroot}/%{_datadir}/sgml/%{name}-%{version}/

# Add unversioned/versioned catalog and symlink
mkdir -p %{buildroot}/etc/sgml
pushd %{buildroot}/etc/sgml
touch %{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{name}.soc
popd

rm -f %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/*.la

%post
%{_bindir}/install-catalog --add %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>/dev/null || :

%preun
%{_bindir}/install-catalog --remove %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>/dev/null || :

# The install-catalog removes the file making uninstallation throw a warning about removing a non-existent file
# This file creation suppresses the warning
touch %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc

%files
%doc jadedoc/* dsssl/README.jadetex
%doc README COPYING VERSION
# Removed %%ghost for succesful instalation on OSTree
%verify(not size filedigest mtime) %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/sgml/%{name}-%{version}

%changelog
%{?autochangelog}
