# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-hack
Version:        3.003
Release:        %autorelease
Summary:        A typeface designed for source code
License:        Bitstream-Vera AND MIT
URL:            http://sourcefoundry.org/hack/
VCS:            git:https://github.com/source-foundry/Hack
#!RemoteAsset:  sha256:3c6f1a20e86744077e83c9bacf879a5b13f659f1c07e9c5c57d6efc3cbe66c07
Source0:        https://github.com/source-foundry/Hack/archive/refs/tags/v%{version}.tar.gz

# use python3 and ignore warning.
Patch2000:      2000-fix-build-error.patch

BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(fontmake)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(python3)
BuildRequires:  ttfautohint
BuildRequires:  make

%description
Hack is designed to be a workhorse typeface for source code. It has deep roots
in the free, open source typeface community and expands upon the contributions
of the Bitstream Vera & DejaVu projects.
The large x-height + wide aperture + low contrast design make it legible at
commonly used source code text sizes with a sweet spot that runs in the
8 - 14 range.

%prep
%autosetup -p1 -n Hack-%{version}

%build
# Build TTF fonts from UFO source
make ttf

%install
mkdir -p %{buildroot}%{_datadir}/fonts/truetype
install -m644 build/ttf/*.ttf %{buildroot}%{_datadir}/fonts/truetype
install -d %{buildroot}%{_docdir}/%{name}
install -m644 LICENSE.md README.md %{buildroot}%{_docdir}/%{name}

%files
%dir %{_datadir}/fonts/truetype
%{_datadir}/fonts/truetype/*.ttf
%doc %{_docdir}/fonts-hack

%changelog
%autochangelog
