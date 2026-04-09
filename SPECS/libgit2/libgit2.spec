# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libgit2
Version:        1.9.2
Release:        %autorelease
Summary:        C implementation of the Git core methods as a library with a solid API
License:        GPL-2.0-only WITH GCC-exception-2.0
URL:            https://libgit2.org/
VCS:            git:https://github.com/libgit2/libgit2
#!RemoteAsset
Source:         https://github.com/libgit2/libgit2/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DREGEX_BACKEND=pcre2
BuildOption(conf):  -DBUILD_CLI=OFF
BuildOption(conf):  -DUSE_HTTP_PARSER=llhttp
BuildOption(conf):  -DUSE_SHA1=HTTPS
BuildOption(conf):  -DUSE_HTTPS=OpenSSL
BuildOption(conf):  -DUSE_NTLMCLIENT=OFF
BuildOption(conf):  -DUSE_SSH=ON

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libllhttp)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  python3
BuildRequires:  pkgconfig(zlib)

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries, header files, and examples for
developing applications that use %{name}.

%prep -a
# Don't run "online" tests
sed -i '/-sonline/s/^/#/' tests/libgit2/CMakeLists.txt

%files
%license COPYING
%{_libdir}/libgit2.so.1.9*

%files devel
%doc AUTHORS docs examples README.md
%{_libdir}/libgit2.so
%{_libdir}/cmake/libgit2/
%{_libdir}/pkgconfig/libgit2.pc
%{_includedir}/git2.h
%{_includedir}/git2/

%changelog
%autochangelog
