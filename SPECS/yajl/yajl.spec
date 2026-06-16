# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           yajl
Version:        2.1.0
Release:        %autorelease
Summary:        A fast streaming JSON parsing library in C
License:        ISC
URL:            https://github.com/lloyd/yajl
#!RemoteAsset:  sha256:3fb73364a5a30efe615046d07e6db9d09fd2b41c763c5f7d3bfb121cd5c5ac5a
Source:         https://github.com/lloyd/yajl/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake

%patchlist
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0001-pkg-config-file-should-be-in-lib-dir-not-shared-data.patch
1000-pkg-config-file-should-be-in-lib-dir-not-shared-data.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0002-pkg-config-include-dir-should-not-have-the-yajl-suff.patch
1001-pkg-config-include-dir-should-not-have-the-yajl-suff.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0003-fix-patch-to-test-files-to-take-account-of-vpath.patch
1002-fix-patch-to-test-files-to-take-account-of-vpath.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0004-drop-bogus-_s-suffix-from-yajl-dynamic-library.patch
1003-drop-bogus-_s-suffix-from-yajl-dynamic-library.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0005-Fix-for-CVE-2017-16516.patch
1004-Fix-for-CVE-2017-16516.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0006-Fix-CVE-2022-24795.patch
1005-Fix-CVE-2022-24795.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0007-yajl-fix-memory-leak-problem.patch
1006-yajl-fix-memory-leak-problem.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0008-fix-memory-leaks.patch
1007-fix-memory-leaks.patch
# https://src.fedoraproject.org/rpms/yajl/blob/rawhide/f/0009-Allow-cmake-4.0.patch
1008-Allow-cmake-4.0.patch

%description
A fast streaming JSON parsing library in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
# No static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/libyajl_s.a

%files
%doc ChangeLog README TODO
%license COPYING
%{_bindir}/json_reformat
%{_bindir}/json_verify
%{_libdir}/libyajl.so.2
%{_libdir}/libyajl.so.2.*

%files devel
%dir %{_includedir}/yajl
%{_includedir}/yajl/yajl_common.h
%{_includedir}/yajl/yajl_gen.h
%{_includedir}/yajl/yajl_parse.h
%{_includedir}/yajl/yajl_tree.h
%{_includedir}/yajl/yajl_version.h
%{_libdir}/libyajl.so
%{_libdir}/pkgconfig/yajl.pc

%changelog
%autochangelog
