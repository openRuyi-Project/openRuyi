# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-linux-build
Version:        20260713
Release:        %autorelease
Summary:        Dependencies for building linux kernel on openRuyi
License:        MulanPSL-2.0
URL:            https://github.com/openRuyi-Project/openRuyi
BuildArch:      noarch

# Actual dependencies for build linux itself
Requires:       gcc
Requires:       bison
Requires:       binutils
Requires:       glibc-devel
Requires:       make
Requires:       perl
Requires:       flex
Requires:       bc
Requires:       cpio
Requires:       dwarves
Requires:       gettext
Requires:       python3
Requires:       rsync
Requires:       tar
Requires:       xz
Requires:       zstd
Requires:       libdebuginfod-dummy-devel
Requires:       pkgconfig(ncurses)
Requires:       pkgconfig(libcap)
Requires:       pkgconfig(libssh)
Requires:       pkgconfig(libdw)
Requires:       pkgconfig(libelf)
Requires:       pkgconfig(libzstd)
Requires:       pkgconfig(python3)
Requires:       pkgconfig(slang)
Requires:       pkgconfig(zlib)
Requires:       pkgconfig(openssl)
Requires:       kmod
Requires:       rpm-config-openruyi

# oR RPM macros
Requires:       %{name}-rpm-macros = %{version}-%{release}

%sourcelist
macros.linux

%description
This package pulls in dependencies for build linux on openRuyi.

%package rpm-macros
Summary:        RPM macros for building linux
# RPM owns the directories we need
Requires:       rpm

%description    rpm-macros
This package contains the RPM macros for building the openRuyi Linux kernel.

%prep
%autosetup -c -T
cp -p %{sources} .

%install
install -p -Dm 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.linux

%files

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.linux

%changelog
%autochangelog
