# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jbigkit
Version:        2.1
Release:        %autorelease
Summary:        JBIG1 lossless image compression tools
License:        GPL-2.0-or-later
URL:            http://www.cl.cam.ac.uk/~mgk25/jbigkit/
# VCS: No git repo found.
#!RemoteAsset
Source0:        http://www.cl.cam.ac.uk/~mgk25/download/jbigkit-%{version}.tar.gz
BuildSystem:    autotools

# Enable shared library build
Patch0:         0001-jbigkit-2.1-shlib.patch
# Fix unused result warnings
Patch1:         0002-jbigkit-2.0-warnings.patch
# patch for coverity issues - backported from upstream
Patch2:         0003-jbigkit-covscan.patch

BuildRequires:  make
BuildRequires:  gcc

%description
JBIG-KIT provides ready-to-use compression and decompression programs with a
simple command line interface for the JBIG1 standard (ISO/IEC 11544).

%package        devel
Summary:        Development files for jbigkit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The jbigkit-devel package contains files needed for development using
the JBIG-KIT image compression library.

# No configure.
%conf

# No install.
%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -p -m0755 libjbig/libjbig.so.* %{buildroot}%{_libdir}
install -p -m0755 libjbig/libjbig85.so.* %{buildroot}%{_libdir}
ln -sf libjbig.so.* %{buildroot}%{_libdir}/libjbig.so
ln -sf libjbig85.so.* %{buildroot}%{_libdir}/libjbig85.so

install -p -m0644 libjbig/jbig.h %{buildroot}%{_includedir}
install -p -m0644 libjbig/jbig85.h %{buildroot}%{_includedir}
install -p -m0644 libjbig/jbig_ar.h %{buildroot}%{_includedir}

install -p -m0755 pbmtools/jbgtopbm %{buildroot}%{_bindir}
install -p -m0755 pbmtools/jbgtopbm85 %{buildroot}%{_bindir}
install -p -m0755 pbmtools/pbmtojbg %{buildroot}%{_bindir}
install -p -m0755 pbmtools/pbmtojbg85 %{buildroot}%{_bindir}
install -p -m0644 pbmtools/*.1 %{buildroot}%{_mandir}/man1

%check
# have to run tests in serial
make test -j1

%files
%license COPYING
%{_bindir}/jbgtopbm
%{_bindir}/jbgtopbm85
%{_bindir}/pbmtojbg
%{_bindir}/pbmtojbg85
%{_mandir}/man1/jbgtopbm.1*
%{_mandir}/man1/pbmtojbg.1*
%{_libdir}/libjbig.so.*
%{_libdir}/libjbig85.so.*

%files devel
%{_libdir}/libjbig.so
%{_libdir}/libjbig85.so
%{_includedir}/jbig*.h

%changelog
%autochangelog
