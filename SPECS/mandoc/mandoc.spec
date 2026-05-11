# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target regress

Name:           mandoc
Version:        1.14.6
Release:        %autorelease
Summary:        UNIX manpage compiler
License:        ISC
URL:            https://mandoc.bsd.lv/
# VCS: TODO: This project use CVS
#!RemoteAsset:  sha256:8bf0d570f01e70a6e124884088870cbed7537f36328d512909eb10cd53179d9c
Source:         https://mandoc.bsd.lv/snapshots/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  pkgconfig(zlib)

%description
The mandoc manpage compiler toolset (formerly called "mdocml")
is a suite of tools compiling mdoc(7), the roff(7) macro language
of choice for BSD manual pages, and man(7), the predominant
historical language for UNIX manuals.

It includes a man(1) manual viewer and additional tools.
For general information, see <http://mandoc.bsd.lv/>.

%conf -p
cat > configure.local << 'EOF'
PREFIX=%{_prefix}
BINDIR=%{_bindir}
SBINDIR=%{_sbindir}
MANDIR=%{_mandir}
INCLUDEDIR=%{_includedir}
LIBDIR=%{_libdir}
LN="ln -sf"
MANM_MANCONF=mandoc.conf
INSTALL_PROGRAM="${INSTALL} -m 0755"
INSTALL_LIB="${INSTALL} -m 0755"
INSTALL_MAN="${INSTALL} -m 0644"
INSTALL_DATA="${INSTALL} -m 0644"
INSTALL_LIBMANDOC=1
CFLAGS="%{optflags} -fPIC"
EOF

%install -a
find %{buildroot} -type f -name "*.a" -delete -print

%files
%license LICENSE
%{_includedir}/*.h
%{_bindir}/apropos
%{_bindir}/demandoc
%{_bindir}/man
%{_bindir}/mandoc
%{_bindir}/soelim
%{_bindir}/whatis
%{_sbindir}/makewhatis
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
