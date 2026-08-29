# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-firacode-nerd
Version:        3.4.0
Release:        %autorelease
Summary:        Fira Code Nerd Font
License:        OFL-1.1
URL:            https://www.nerdfonts.com/
VCS:            git:https://github.com/ryanoasis/nerd-fonts.git
#!RemoteAsset:  sha256:d83fb093e0e05a531cd6f19886a6ceb884a4fa5ea3b53cf099fc1f30c5b3e47d
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/FiraCode.tar.xz
BuildArch:      noarch

%description
Fira Code Nerd Font is a patched version of Fira Code with icons from Nerd
Fonts.

%prep
%autosetup -c

%build
# No build required

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts/truetype/firacode-nerd
install -m 0644 -p *.ttf %{buildroot}%{_datadir}/fonts/truetype/firacode-nerd/

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/fonts/truetype/firacode-nerd/
%{_datadir}/fonts/truetype/firacode-nerd/*.ttf

%changelog
%autochangelog
