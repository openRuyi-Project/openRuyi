# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rpminspect
Version:        2.1
Release:        %autorelease
Summary:        Build deviation analysis and compliance tool
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND Apache-2.0 AND MIT AND BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0
URL:            https://github.com/rpminspect/rpminspect
#!RemoteAsset:  sha256:9b9cec725aac9ec21f54725c11a5a642066e725ee991699014a4a51bdfc6caa2
Source0:        https://github.com/rpminspect/rpminspect/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    meson

# We don't want tons of python dependencies like rpmfluff
BuildOption(conf):  -D tests=false

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(xmlrpc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  rpm-devel
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libclamav)
BuildRequires:  mandoc
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(cdson)

Recommends:     rpm-config-openruyi
Recommends:     dash
Recommends:     ksh
Recommends:     zsh
Recommends:     tcsh
Recommends:     rc
Recommends:     bash
Recommends:     clamav

Requires:       desktop-file-utils
Requires:       gettext

%description
Build deviation and compliance tool.  This program runs a number of tests
against one or two builds of source RPM files.  The built artifacts are
inspected and compared to report changes and validate policy compliance
against the defined parameters.

%package        devel
Summary:        Header files and development libraries for rpminspect
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The header files and development library links required to build software
using rpminspect.

%prep -a
# not always compatible with new warnings in latest GCC (particularly libtoml)
sed -i -e 's|werror=true|werror=false|' meson.build

%install -a
# TODO: We should use system libraries in the future
# Install bundled library docs and licenses
install -D -m 0644 libxdiff/AUTHORS %{buildroot}%{_pkgdocdir}/libxdiff/AUTHORS
install -D -m 0644 libxdiff/README %{buildroot}%{_pkgdocdir}/libxdiff/README
install -D -m 0644 libxdiff/COPYING %{buildroot}%{_datadir}/licenses/%{name}/libxdiff/COPYING

install -D -m 0644 libtoml/README.md %{buildroot}%{_pkgdocdir}/libtoml/README.md
install -D -m 0644 libtoml/README.rpminspect %{buildroot}%{_pkgdocdir}/libtoml/README.rpminspect
install -D -m 0644 libtoml/LICENSE %{buildroot}%{_datadir}/licenses/%{name}/libtoml/LICENSE

%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc AUTHORS.md CHANGES.md README.md TODO
%doc %{_pkgdocdir}/libxdiff/AUTHORS
%doc %{_pkgdocdir}/libxdiff/README
%doc %{_pkgdocdir}/libtoml/README.md
%doc %{_pkgdocdir}/libtoml/README.rpminspect
%license %{_datadir}/licenses/%{name}/libxdiff/COPYING
%license %{_datadir}/licenses/%{name}/libtoml/LICENSE
%license COPYING COPYING.LIB LICENSE-2.0.txt MIT.txt CC-BY-4.0.txt
%{_bindir}/rpminspect
%{_libdir}/librpminspect.so.*
%{_datadir}/rpminspect
%{_mandir}/man1/rpminspect.1*

%files devel
%license COPYING.LIB
%{_includedir}/librpminspect
%{_libdir}/librpminspect.so

%changelog
%autochangelog
