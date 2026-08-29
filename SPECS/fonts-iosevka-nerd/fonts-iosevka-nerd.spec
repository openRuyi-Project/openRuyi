# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-iosevka-nerd
Version:        3.4.0
Release:        %autorelease
Summary:        Iosevka Nerd Font
License:        OFL-1.1
URL:            https://www.nerdfonts.com/
VCS:            git:https://github.com/ryanoasis/nerd-fonts.git
#!RemoteAsset:  sha256:213ee24cda99ca84d0a8326de133e7e8b2baf9ba23659ce829f589f771d357d2
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/Iosevka.tar.xz
BuildArch:      noarch

%description
Iosevka Nerd Font is a patched version of Iosevka with icons from Nerd Fonts.

%prep
%autosetup -c

%build
# No build required

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts/truetype/iosevka-nerd
install -m 0644 -p *.ttf %{buildroot}%{_datadir}/fonts/truetype/iosevka-nerd/

%files
%doc README.md
%license LICENSE.md
%dir %{_datadir}/fonts/truetype/iosevka-nerd/
%{_datadir}/fonts/truetype/iosevka-nerd/*.ttf

%changelog
%autochangelog
