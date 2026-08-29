# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-jetbrainsmono-nerd
Version:        3.4.0
Release:        %autorelease
Summary:        JetBrains Mono Nerd Font
License:        OFL-1.1
URL:            https://www.nerdfonts.com/
VCS:            git:https://github.com/ryanoasis/nerd-fonts.git
#!RemoteAsset:  sha256:ef552a3e638f25125c6ad4c51176a6adcdce295ab1d2ffacf0db060caf8c1582
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.tar.xz
BuildArch:      noarch

%description
JetBrains Mono Nerd Font is a patched version of JetBrains Mono with icons
from Nerd Fonts.

%prep
%autosetup -c

%build
# No build required

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts/truetype/jetbrainsmono-nerd
install -m 0644 -p *.ttf %{buildroot}%{_datadir}/fonts/truetype/jetbrainsmono-nerd/

%files
%license OFL.txt
%dir %{_datadir}/fonts/truetype/jetbrainsmono-nerd/
%{_datadir}/fonts/truetype/jetbrainsmono-nerd/*.ttf

%changelog
%autochangelog
