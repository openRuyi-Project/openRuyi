# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libunistring
Version:        1.4.2
Release:        %autorelease
Summary:        GNU Unicode string library
License:        GPL-3.0-or-later OR LGPL-3.0-or-later
URL:            https://www.gnu.org/software/libunistring/
VCS:            git:https://https.git.savannah.gnu.org/git/libunistring.git
#!RemoteAsset:  sha256:5b46e74377ed7409c5b75e7a96f95377b095623b689d8522620927964a41499c
Source0:        http://ftpmirror.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
BuildSystem:    autotools

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package        devel
Summary:        Development files for the GNU Unicode string library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for programs using libunistring and documentation
for UniString library.

%package        static
Summary:        Static version of libunistring library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
Static library for the %{name} library

%files
%license COPYING*
%{_libdir}/libunistring.so.*

%files devel
%license COPYING*
%{_docdir}/%{name}
%{_infodir}/libunistring.info*
%{_libdir}/libunistring.so
%{_includedir}/unistring
%{_includedir}/*.h

%files static
%license COPYING*
%{_libdir}/libunistring.a

%changelog
%autochangelog
