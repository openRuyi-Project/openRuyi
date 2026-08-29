# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmlrpc-c
Version:        1.64.03
Release:        %autorelease
Summary:        A lightweight RPC library based on XML and HTTP
License:        BSD-3-Clause AND MIT
URL:            https://xmlrpc-c.sourceforge.io
# VCS: No VCS link available
#!RemoteAsset:  sha256:74729d364edbedbe42e782822da1e076f3f45c65c4278a3cfba5f2342d7cedbe
Source0:        http://downloads.sourceforge.net/xmlrpc-c/xmlrpc-%{version}.tgz#/%{name}-%{version}.tgz
BuildSystem:    autotools

# Serial build required: upstream's recursive makefiles miss a dependency
# between the .osh shared objects and the .so link target, so a parallel
# build races (the .so link starts before its .osh inputs finish). With
# LTO this surfaces as a fatal "resolution sub id not in object file" ICE.
BuildOption(build):  CFLAGS="%{optflags} -std=gnu17" --jobs 1
BuildOption(check):  CFLAGS="%{optflags} -std=gnu17" --jobs 1

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(ncurses)

%description
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

%package        devel
Summary:        Development files for xmlrpc-c based programs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This package provides static libraries and header files for writing
XML-RPC applications in C and C++.

%files
%doc doc/CREDITS doc/HISTORY
%doc tools/xmlrpc_transport/xmlrpc_transport.html
%license doc/COPYING lib/abyss/license.txt
%{_libdir}/libxmlrpc_xml*.so.*
%{_libdir}/libxmlrpc.so.*
%{_libdir}/libxmlrpc_openssl.so.*
%{_libdir}/libxmlrpc_util.so.*
%{_libdir}/libxmlrpc_abyss.so.*
%{_libdir}/libxmlrpc_server.so.*
%{_libdir}/libxmlrpc_server_abyss.so.*
%{_libdir}/libxmlrpc_server_cgi.so.*
%exclude %{_libdir}/libxmlrpc*.a
# Client
%{_libdir}/libxmlrpc_client.so.*
%{_libdir}/libxmlrpc_client++.so.*
# C++
%{_libdir}/libxmlrpc_cpp.so.*
%{_libdir}/libxmlrpc++.so.*
%{_libdir}/libxmlrpc_util++.so.*
%{_libdir}/libxmlrpc_abyss++.so.*
%{_libdir}/libxmlrpc_server++.so.*
%{_libdir}/libxmlrpc_server_abyss++.so.*
%{_libdir}/libxmlrpc_server_cgi++.so.*
%{_libdir}/libxmlrpc_packetsocket.so.*
%{_libdir}/libxmlrpc_server_pstream++.so.*

%files devel
%{_bindir}/xmlrpc-c-config
%{_includedir}/xmlrpc-c/
%{_includedir}/*.h
%{_libdir}/pkgconfig/xmlrpc.pc
%{_libdir}/pkgconfig/xmlrpc++.pc
%{_libdir}/pkgconfig/xmlrpc_abyss++.pc
%{_libdir}/pkgconfig/xmlrpc_abyss.pc
%{_libdir}/pkgconfig/xmlrpc_client++.pc
%{_libdir}/pkgconfig/xmlrpc_client.pc
%{_libdir}/pkgconfig/xmlrpc_expat.pc
%{_libdir}/pkgconfig/xmlrpc_openssl.pc
%{_libdir}/pkgconfig/xmlrpc_server++.pc
%{_libdir}/pkgconfig/xmlrpc_server.pc
%{_libdir}/pkgconfig/xmlrpc_server_abyss.pc
%{_libdir}/pkgconfig/xmlrpc_server_cgi.pc
%{_libdir}/pkgconfig/xmlrpc_server_pstream++.pc
%{_libdir}/pkgconfig/xmlrpc_util++.pc
%{_libdir}/pkgconfig/xmlrpc_util.pc
%{_libdir}/libxmlrpc*.so

%changelog
%autochangelog
