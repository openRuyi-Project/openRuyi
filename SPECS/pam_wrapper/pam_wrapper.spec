# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pam_wrapper
Version:        1.1.8
Release:        %autorelease
Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
URL:            http://cwrap.org/
VCS:            git:https://git.samba.org/pam_wrapper.git
#!RemoteAsset:  sha256:6549c0b3e41d1ebe0c94a1be63c25eec918191462b602ab6f47d4a5fa709c3e4
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:6093195d65f7e3566f38e3d9f9e0b6c3615e92774de904028937b18d941f699b
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption(conf):  -DUNIT_TESTING=ON
BuildOption(conf):  -DPYTHON_INSTALL_SITEARCH=%{python3_sitearch}

BuildRequires:  cmake
BuildRequires:  cmocka-cmake
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(pam)

Recommends:     cmake
Recommends:     pkgconfig

%description
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module.

For testing PAM applications, simple PAM module called pam_matrix is
included. If you plan to test a PAM module you can use the pamtest library,
which simplifies testing of modules. You can combine it with the cmocka
unit testing framework or you can use the provided Python bindings to
write tests for your module in Python.

%package     -n libpamtest
Summary:        A tool to test PAM applications and PAM modules
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       pam_wrapper = %{version}-%{release}

%description -n libpamtest
If you plan to test a PAM module you can use this library, which simplifies
testing of modules.

%package     -n libpamtest-devel
Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
Requires:       pam_wrapper = %{version}-%{release}
Requires:       libpamtest = %{version}-%{release}
Recommends:     cmake
Recommends:     pkgconfig

%description -n libpamtest-devel
If you plan to develop tests for a PAM module you can use this library,
which simplifies testing of modules. This sub package includes the header
files for libpamtest.

%package     -n python-libpamtest
Summary:        A python wrapper for libpamtest
License:        GPL-3.0-or-later
Provides:       python3-libpamtest
%python_provide python3-libpamtest
Requires:       pam_wrapper = %{version}-%{release}
Requires:       libpamtest = %{version}-%{release}

%description -n python-libpamtest
If you plan to develop python tests for a PAM module you can use this
Python module to quickly write tests in Python

%prep -a
# Not compatible with Python 3.12 headers
sed -i -e '/Werror=declaration-after-statement/d' CompilerChecks.cmake
# renamed in Python 3.2, old name dropped in 3.12
sed -i -e 's/assertRaisesRegexp/assertRaisesRegex/' tests/pypamtest_test.py

%files
%{_libdir}/libpam_wrapper.so*
%{_libdir}/pkgconfig/pam_wrapper.pc
%dir %{_libdir}/cmake/pam_wrapper
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config-version.cmake
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config.cmake
%{_libdir}/pam_wrapper/pam_chatty.so
%{_libdir}/pam_wrapper/pam_matrix.so
%{_libdir}/pam_wrapper/pam_get_items.so
%{_libdir}/pam_wrapper/pam_set_items.so
%{_mandir}/man1/pam_wrapper.1*
%{_mandir}/man8/pam_chatty.8*
%{_mandir}/man8/pam_matrix.8*
%{_mandir}/man8/pam_get_items.8*
%{_mandir}/man8/pam_set_items.8*

%files -n libpamtest
%{_libdir}/libpamtest.so.*

%files -n libpamtest-devel
%{_libdir}/libpamtest.so
%{_libdir}/pkgconfig/libpamtest.pc
%dir %{_libdir}/cmake/pamtest
%{_libdir}/cmake/pamtest/pamtest-config-relwithdebinfo.cmake
%{_libdir}/cmake/pamtest/pamtest-config-version.cmake
%{_libdir}/cmake/pamtest/pamtest-config.cmake
%{_includedir}/libpamtest.h

%files -n python-libpamtest
%{python3_sitearch}/pypamtest.so

%changelog
%autochangelog
