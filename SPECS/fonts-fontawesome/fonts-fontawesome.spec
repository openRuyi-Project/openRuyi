# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-fontawesome
Version:        6.7.2
Release:        %autorelease
Summary:        Iconic font set
License:        OFL-1.1
URL:            https://fontawesome.com/
VCS:            git:https://github.com/FortAwesome/Font-Awesome.git
#!RemoteAsset:  sha256:22ff7898b429b997a45e1cf89bb869ed3abcc65333d90289181ba5363c8fd19b
Source0:        https://github.com/FortAwesome/Font-Awesome/releases/download/%{version}/fontawesome-free-%{version}-desktop.zip
#!RemoteAsset:  sha256:ecdaaa6d347cd7da82c66054770995e97f3d066a57e8d58ac9c517f0f77561fb
Source1:        https://github.com/FortAwesome/Font-Awesome/releases/download/%{version}/fontawesome-free-%{version}-web.zip
BuildArch:      noarch

BuildRequires:  fonts-rpm-macros
BuildRequires:  unzip

%description
Scalable vector icons that can be customized: size, color, drop shadow,
and anything that can be done with the power of CSS.

(Note that the font does not contain regular letters, and that icons
are in the range U+F000..U+F23A.)

%package        web
Summary:        Web files for Font Awesome
License:        MIT

%description    web
Web files for Font Awesome.

%prep
%setup -q -c
%setup -q -T -D -a 1

%build

%install
%install_fonts */otfs/*.otf fontawesome
%install_fonts */webfonts/*.ttf fontawesome

install -m 0755 -d %{buildroot}%{_datadir}/webfonts/fontawesome
install -p -m 0644 */webfonts/*.woff2 %{buildroot}%{_datadir}/webfonts/fontawesome

install -m 0755 -d %{buildroot}%{_datadir}/fontawesome-web
cp -pr */css */less */scss %{buildroot}%{_datadir}/fontawesome-web/

%files
%license fontawesome-free-%{version}-desktop/LICENSE.txt
%font_files fontawesome ttf otf

%files web
%license fontawesome-free-%{version}-web/LICENSE.txt
%{_datadir}/fontawesome-web/
%{_datadir}/webfonts/fontawesome/

%changelog
%autochangelog
