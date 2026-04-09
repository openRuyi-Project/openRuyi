# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           obs-build
Version:        20250829
Release:        %autorelease
Summary:        A Script to Build Linux RPMs
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://github.com/openSUSE/obs-build
#!RemoteAsset
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(POSIX)

# Of course
Provides:       build = %{version}-%{release}

Requires:       %{name}-mkbaselibs = %{version}-%{release}
Requires:       bash
Requires:       binutils
Requires:       perl
Requires:       tar

Recommends:     %{name}-mkdrpms = %{version}-%{release}
Recommends:     perl(Config::IniFiles)
Recommends:     perl(Date::Language)
Recommends:     perl(Date::Parse)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Pod::Usage)
Recommends:     perl(Time::Zone)
Recommends:     perl(URI)
Recommends:     perl(XML::Parser)
Recommends:     perl(YAML::LibYAML)

%description
This package provides a script for building RPMs in a chroot environment.

%package        mkbaselibs
Summary:        Tools to generate base lib packages

%description    mkbaselibs
This package contains the parts which may be installed in the inner build system
for generating base lib packages.

%package        mkdrpms
Summary:        Tools to generate delta rpms
Requires:       deltarpm
Requires:       %{name}

%description    mkdrpms
This package contains the parts which may be installed in the inner build system
for generating delta rpm packages.

%prep
%autosetup -p1

%conf
# No conf

%build
# No build

%install
%make_install
pushd %{buildroot}%{_libdir}/build/configs/
touch default.conf
test -e default.conf
popd

# Install man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 build.1* %{buildroot}%{_mandir}/man1/
install -m 0644 buildvc.1* %{buildroot}%{_mandir}/man1/
install -m 0644 unrpm.1* %{buildroot}%{_mandir}/man1/

# Fix Python shebang for openstack-console
sed -e "s|#!/usr/bin/python|#!%{__python3}|" \
    -i %{buildroot}%{_libdir}/build/openstack-console

%files
%license COPYING
%doc README.md
%{_bindir}/build
%{_bindir}/buildvc
%{_bindir}/unrpm
%{_bindir}/pbuild
%{_libdir}/build
%{_mandir}/man1/build.1*
%{_mandir}/man1/buildvc.1*
%{_mandir}/man1/unrpm.1*
%{_mandir}/man1/pbuild.1*
%exclude %{_libdir}/build/mkbaselibs
%exclude %{_libdir}/build/baselibs*
%exclude %{_libdir}/build/mkdrpms

%files mkbaselibs
%{_libdir}/build/mkbaselibs
%{_libdir}/build/baselibs*

%files mkdrpms
%{_libdir}/build/mkdrpms

%changelog
%autochangelog
