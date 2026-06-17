# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-ui-kit
%global full_version 0.3.2
%global pkgname objc2-ui-kit-0.3

Name:           rust-objc2-ui-kit-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-ui-kit"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:d87d638e33c06f577498cbcc50491496a3ed4246998a7fbba7ccb98b1e7eab22
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/documentmanager) = %{version}
Provides:       crate(%{pkgname}/nsfileproviderextension) = %{version}
Provides:       crate(%{pkgname}/nstext) = %{version}
Provides:       crate(%{pkgname}/nstextviewportlayoutcontroller) = %{version}
Provides:       crate(%{pkgname}/nstoolbar-uikitadditions) = %{version}
Provides:       crate(%{pkgname}/nstouchbar-uikitadditions) = %{version}
Provides:       crate(%{pkgname}/nsuseractivity-nsitemprovider) = %{version}
Provides:       crate(%{pkgname}/printkitui) = %{version}
Provides:       crate(%{pkgname}/sharesheet) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/uiaccessibilitycontentsizecategoryimageadjusting) = %{version}
Provides:       crate(%{pkgname}/uiaccessibilityzoom) = %{version}
Provides:       crate(%{pkgname}/uialert) = %{version}
Provides:       crate(%{pkgname}/uibandselectioninteraction) = %{version}
Provides:       crate(%{pkgname}/uibarcommon) = %{version}
Provides:       crate(%{pkgname}/uibehavioralstyle) = %{version}
Provides:       crate(%{pkgname}/uicalendarselection) = %{version}
Provides:       crate(%{pkgname}/uicalendarviewdecoration) = %{version}
Provides:       crate(%{pkgname}/uicanvasfeedbackgenerator) = %{version}
Provides:       crate(%{pkgname}/uiconfigurationcolortransformer) = %{version}
Provides:       crate(%{pkgname}/uicontentsizecategoryadjusting) = %{version}
Provides:       crate(%{pkgname}/uicontextmenusystem) = %{version}
Provides:       crate(%{pkgname}/uifeedbackgenerator) = %{version}
Provides:       crate(%{pkgname}/uifocusdebugger) = %{version}
Provides:       crate(%{pkgname}/uifocusdefines) = %{version}
Provides:       crate(%{pkgname}/uifocussystem) = %{version}
Provides:       crate(%{pkgname}/uifocusupdatecontext-uikitadditions) = %{version}
Provides:       crate(%{pkgname}/uifoundation) = %{version}
Provides:       crate(%{pkgname}/uiguidedaccessrestrictions) = %{version}
Provides:       crate(%{pkgname}/uiimpactfeedbackgenerator) = %{version}
Provides:       crate(%{pkgname}/uiinputsuggestion) = %{version}
Provides:       crate(%{pkgname}/uiinterface) = %{version}
Provides:       crate(%{pkgname}/uikeyconstants) = %{version}
Provides:       crate(%{pkgname}/uikitcore) = %{version}
Provides:       crate(%{pkgname}/uikitdefines) = %{version}
Provides:       crate(%{pkgname}/uiletterformawareadjusting) = %{version}
Provides:       crate(%{pkgname}/uimenusystem) = %{version}
Provides:       crate(%{pkgname}/uimessageconversationcontext) = %{version}
Provides:       crate(%{pkgname}/uimessageconversationentry) = %{version}
Provides:       crate(%{pkgname}/uinibdeclarations) = %{version}
Provides:       crate(%{pkgname}/uinotificationfeedbackgenerator) = %{version}
Provides:       crate(%{pkgname}/uipointerinteraction) = %{version}
Provides:       crate(%{pkgname}/uipopoverpresentationcontrollersourceitem) = %{version}
Provides:       crate(%{pkgname}/uipresentationcontroller) = %{version}
Provides:       crate(%{pkgname}/uipreviewinteraction) = %{version}
Provides:       crate(%{pkgname}/uiresponder-uiactivityitemsconfiguration) = %{version}
Provides:       crate(%{pkgname}/uiscene-avaudiosession) = %{version}
Provides:       crate(%{pkgname}/uisceneenhancedstaterestoration) = %{version}
Provides:       crate(%{pkgname}/uiscenesizerestrictions) = %{version}
Provides:       crate(%{pkgname}/uiscenewindowingbehaviors) = %{version}
Provides:       crate(%{pkgname}/uiscenewindowingcontrolstyle) = %{version}
Provides:       crate(%{pkgname}/uiscreenmode) = %{version}
Provides:       crate(%{pkgname}/uiscribbleinteraction) = %{version}
Provides:       crate(%{pkgname}/uiscrolledgeelementcontainerinteraction) = %{version}
Provides:       crate(%{pkgname}/uiselectionfeedbackgenerator) = %{version}
Provides:       crate(%{pkgname}/uisnapbehavior) = %{version}
Provides:       crate(%{pkgname}/uisplitviewcontrollerlayoutenvironment) = %{version}
Provides:       crate(%{pkgname}/uispringloadedinteraction) = %{version}
Provides:       crate(%{pkgname}/uispringloadedinteractionsupporting) = %{version}
Provides:       crate(%{pkgname}/uistatusbarmanager) = %{version}
Provides:       crate(%{pkgname}/uisymboleffectcompletion) = %{version}
Provides:       crate(%{pkgname}/uitabaccessory) = %{version}
Provides:       crate(%{pkgname}/uitextcursordroppositionanimator) = %{version}
Provides:       crate(%{pkgname}/uitextcursorview) = %{version}
Provides:       crate(%{pkgname}/uitextinputcontext) = %{version}
Provides:       crate(%{pkgname}/uitextiteminteraction) = %{version}
Provides:       crate(%{pkgname}/uitextloupesession) = %{version}
Provides:       crate(%{pkgname}/uitextpasteconfigurationsupporting) = %{version}
Provides:       crate(%{pkgname}/uitextselectionhandleview) = %{version}
Provides:       crate(%{pkgname}/uitraitlistenvironment) = %{version}
Provides:       crate(%{pkgname}/uiupdateactionphase) = %{version}
Provides:       crate(%{pkgname}/uiupdatelink) = %{version}
Provides:       crate(%{pkgname}/uiviewcontrollertransition) = %{version}
Provides:       crate(%{pkgname}/uiviewlayoutregion) = %{version}
Provides:       crate(%{pkgname}/uiwindowsceneactivationrequestoptions) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenedraginteraction) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferences) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesios) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesmac) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesvision) = %{version}
Provides:       crate(%{pkgname}/uiwritingtoolscoordinatoranimationparameters) = %{version}
Provides:       crate(%{pkgname}/unnotificationresponse-uikitadditions) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-ui-kit"

%package     -n %{name}+nsadaptiveimageglyph
Summary:        Bindings to the UIKit framework - feature "NSAdaptiveImageGlyph"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsadaptiveimageglyph) = %{version}

%description -n %{name}+nsadaptiveimageglyph
This metapackage enables feature "NSAdaptiveImageGlyph" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsattributedstring
Summary:        Bindings to the UIKit framework - feature "NSAttributedString"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilewrapper) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsattributedstring) = %{version}

%description -n %{name}+nsattributedstring
This metapackage enables feature "NSAttributedString" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdataasset
Summary:        Bindings to the UIKit framework - feature "NSDataAsset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsdataasset) = %{version}

%description -n %{name}+nsdataasset
This metapackage enables feature "NSDataAsset" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdiffabledatasourcesectionsnapshot
Summary:        Bindings to the UIKit framework - feature "NSDiffableDataSourceSectionSnapshot" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsdiffabledatasourcesectionsnapshot) = %{version}
Provides:       crate(%{pkgname}/nslayoutanchor) = %{version}
Provides:       crate(%{pkgname}/uifont) = %{version}
Provides:       crate(%{pkgname}/uilexicon) = %{version}
Provides:       crate(%{pkgname}/uislidertrackconfiguration) = %{version}
Provides:       crate(%{pkgname}/uitextformattingviewcontrollercomponent) = %{version}

%description -n %{name}+nsdiffabledatasourcesectionsnapshot
This metapackage enables feature "NSDiffableDataSourceSectionSnapshot" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSLayoutAnchor", "UIFont", "UILexicon", "UISliderTrackConfiguration", and "UITextFormattingViewControllerComponent" features.

%package     -n %{name}+nsindexpath-uikitadditions
Summary:        Bindings to the UIKit framework - feature "NSIndexPath_UIKitAdditions" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Provides:       crate(%{pkgname}/nsindexpath-uikitadditions) = %{version}
Provides:       crate(%{pkgname}/uicollectionviewupdateitem) = %{version}
Provides:       crate(%{pkgname}/uidatasourcetranslating) = %{version}

%description -n %{name}+nsindexpath-uikitadditions
This metapackage enables feature "NSIndexPath_UIKitAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICollectionViewUpdateItem", and "UIDataSourceTranslating" features.

%package     -n %{name}+nsitemprovider-uikitadditions
Summary:        Bindings to the UIKit framework - feature "NSItemProvider_UIKitAdditions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsitemprovider-uikitadditions) = %{version}

%description -n %{name}+nsitemprovider-uikitadditions
This metapackage enables feature "NSItemProvider_UIKitAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nslayoutconstraint
Summary:        Bindings to the UIKit framework - feature "NSLayoutConstraint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nslayoutconstraint) = %{version}

%description -n %{name}+nslayoutconstraint
This metapackage enables feature "NSLayoutConstraint" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nslayoutmanager
Summary:        Bindings to the UIKit framework - feature "NSLayoutManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nslayoutmanager) = %{version}

%description -n %{name}+nslayoutmanager
This metapackage enables feature "NSLayoutManager" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsparagraphstyle
Summary:        Bindings to the UIKit framework - feature "NSParagraphStyle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscharacterset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsparagraphstyle) = %{version}

%description -n %{name}+nsparagraphstyle
This metapackage enables feature "NSParagraphStyle" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsshadow
Summary:        Bindings to the UIKit framework - feature "NSShadow" and 18 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nsshadow) = %{version}
Provides:       crate(%{pkgname}/uiactivityindicatorview) = %{version}
Provides:       crate(%{pkgname}/uibackgroundextensionview) = %{version}
Provides:       crate(%{pkgname}/uibarappearance) = %{version}
Provides:       crate(%{pkgname}/uibezierpath) = %{version}
Provides:       crate(%{pkgname}/uicellconfigurationstate) = %{version}
Provides:       crate(%{pkgname}/uicontentunavailableview) = %{version}
Provides:       crate(%{pkgname}/uieventattributionview) = %{version}
Provides:       crate(%{pkgname}/uiimageasset) = %{version}
Provides:       crate(%{pkgname}/uiinputview) = %{version}
Provides:       crate(%{pkgname}/uipagecontrol) = %{version}
Provides:       crate(%{pkgname}/uipastecontrol) = %{version}
Provides:       crate(%{pkgname}/uipopoverbackgroundview) = %{version}
Provides:       crate(%{pkgname}/uislider) = %{version}
Provides:       crate(%{pkgname}/uistandardtextcursorview) = %{version}
Provides:       crate(%{pkgname}/uistepper) = %{version}
Provides:       crate(%{pkgname}/uitoolbarappearance) = %{version}
Provides:       crate(%{pkgname}/uiviewconfigurationstate) = %{version}
Provides:       crate(%{pkgname}/uivisualeffectview) = %{version}

%description -n %{name}+nsshadow
This metapackage enables feature "NSShadow" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIActivityIndicatorView", "UIBackgroundExtensionView", "UIBarAppearance", "UIBezierPath", "UICellConfigurationState", "UIContentUnavailableView", "UIEventAttributionView", "UIImageAsset", "UIInputView", "UIPageControl", "UIPasteControl", "UIPopoverBackgroundView", "UISlider", "UIStandardTextCursorView", "UIStepper", "UIToolbarAppearance", "UIViewConfigurationState", and "UIVisualEffectView" features.

%package     -n %{name}+nsstringdrawing
Summary:        Bindings to the UIKit framework - feature "NSStringDrawing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsstringdrawing) = %{version}

%description -n %{name}+nsstringdrawing
This metapackage enables feature "NSStringDrawing" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextattachment
Summary:        Bindings to the UIKit framework - feature "NSTextAttachment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilewrapper) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextattachment) = %{version}

%description -n %{name}+nstextattachment
This metapackage enables feature "NSTextAttachment" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextcontainer
Summary:        Bindings to the UIKit framework - feature "NSTextContainer" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nstextcontainer) = %{version}
Provides:       crate(%{pkgname}/uicollectionviewlistcell) = %{version}
Provides:       crate(%{pkgname}/uistackview) = %{version}
Provides:       crate(%{pkgname}/uitabbar) = %{version}
Provides:       crate(%{pkgname}/uitoolbar) = %{version}

%description -n %{name}+nstextcontainer
This metapackage enables feature "NSTextContainer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICollectionViewListCell", "UIStackView", "UITabBar", and "UIToolbar" features.

%package     -n %{name}+nstextcontentmanager
Summary:        Bindings to the UIKit framework - feature "NSTextContentManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextcontentmanager) = %{version}

%description -n %{name}+nstextcontentmanager
This metapackage enables feature "NSTextContentManager" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextelement
Summary:        Bindings to the UIKit framework - feature "NSTextElement"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextelement) = %{version}

%description -n %{name}+nstextelement
This metapackage enables feature "NSTextElement" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlayoutfragment
Summary:        Bindings to the UIKit framework - feature "NSTextLayoutFragment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlayoutfragment) = %{version}

%description -n %{name}+nstextlayoutfragment
This metapackage enables feature "NSTextLayoutFragment" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlayoutmanager
Summary:        Bindings to the UIKit framework - feature "NSTextLayoutManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlayoutmanager) = %{version}

%description -n %{name}+nstextlayoutmanager
This metapackage enables feature "NSTextLayoutManager" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlinefragment
Summary:        Bindings to the UIKit framework - feature "NSTextLineFragment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlinefragment) = %{version}

%description -n %{name}+nstextlinefragment
This metapackage enables feature "NSTextLineFragment" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlist
Summary:        Bindings to the UIKit framework - feature "NSTextList" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlist) = %{version}
Provides:       crate(%{pkgname}/uimenuelement) = %{version}
Provides:       crate(%{pkgname}/uitableviewcell) = %{version}

%description -n %{name}+nstextlist
This metapackage enables feature "NSTextList" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIMenuElement", and "UITableViewCell" features.

%package     -n %{name}+nstextlistelement
Summary:        Bindings to the UIKit framework - feature "NSTextListElement"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlistelement) = %{version}

%description -n %{name}+nstextlistelement
This metapackage enables feature "NSTextListElement" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextrange
Summary:        Bindings to the UIKit framework - feature "NSTextRange"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Provides:       crate(%{pkgname}/nstextrange) = %{version}

%description -n %{name}+nstextrange
This metapackage enables feature "NSTextRange" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextselection
Summary:        Bindings to the UIKit framework - feature "NSTextSelection" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextselection) = %{version}
Provides:       crate(%{pkgname}/uinavigationbar) = %{version}
Provides:       crate(%{pkgname}/uisegmentedcontrol) = %{version}

%description -n %{name}+nstextselection
This metapackage enables feature "NSTextSelection" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UINavigationBar", and "UISegmentedControl" features.

%package     -n %{name}+nstextselectionnavigation
Summary:        Bindings to the UIKit framework - feature "NSTextSelectionNavigation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextselectionnavigation) = %{version}

%description -n %{name}+nstextselectionnavigation
This metapackage enables feature "NSTextSelectionNavigation" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextstorage
Summary:        Bindings to the UIKit framework - feature "NSTextStorage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextstorage) = %{version}

%description -n %{name}+nstextstorage
This metapackage enables feature "NSTextStorage" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiaccelerometer
Summary:        Bindings to the UIKit framework - feature "UIAccelerometer" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccelerometer) = %{version}
Provides:       crate(%{pkgname}/uifocusanimationcoordinator) = %{version}
Provides:       crate(%{pkgname}/uipagecontrolprogress) = %{version}
Provides:       crate(%{pkgname}/uipencilinteraction) = %{version}
Provides:       crate(%{pkgname}/uiupdateinfo) = %{version}

%description -n %{name}+uiaccelerometer
This metapackage enables feature "UIAccelerometer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIFocusAnimationCoordinator", "UIPageControlProgress", "UIPencilInteraction", and "UIUpdateInfo" features.

%package     -n %{name}+uiaccessibility
Summary:        Bindings to the UIKit framework - feature "UIAccessibility"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibility) = %{version}

%description -n %{name}+uiaccessibility
This metapackage enables feature "UIAccessibility" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiaccessibilityadditions
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityAdditions" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilityadditions) = %{version}
Provides:       crate(%{pkgname}/uiaccessibilitycustomrotor) = %{version}

%description -n %{name}+uiaccessibilityadditions
This metapackage enables feature "UIAccessibilityAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAccessibilityCustomRotor" feature.

%package     -n %{name}+uiaccessibilityconstants
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityConstants"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilityconstants) = %{version}

%description -n %{name}+uiaccessibilityconstants
This metapackage enables feature "UIAccessibilityConstants" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiaccessibilitycontainer
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityContainer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilitycontainer) = %{version}
Provides:       crate(%{pkgname}/uiprintpagerenderer) = %{version}

%description -n %{name}+uiaccessibilitycontainer
This metapackage enables feature "UIAccessibilityContainer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPrintPageRenderer" feature.

%package     -n %{name}+uiaccessibilitycustomaction
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityCustomAction" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilitycustomaction) = %{version}
Provides:       crate(%{pkgname}/uiaccessibilitylocationdescriptor) = %{version}
Provides:       crate(%{pkgname}/uisearchsuggestion) = %{version}

%description -n %{name}+uiaccessibilitycustomaction
This metapackage enables feature "UIAccessibilityCustomAction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAccessibilityLocationDescriptor", and "UISearchSuggestion" features.

%package     -n %{name}+uiaccessibilityelement
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityElement" and 17 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilityelement) = %{version}
Provides:       crate(%{pkgname}/uiaccessibilityidentification) = %{version}
Provides:       crate(%{pkgname}/uiactivityitemsconfigurationreading-sharesheet) = %{version}
Provides:       crate(%{pkgname}/uicontextualaction) = %{version}
Provides:       crate(%{pkgname}/uidocumentviewcontrollerlaunchoptions) = %{version}
Provides:       crate(%{pkgname}/uifindsession) = %{version}
Provides:       crate(%{pkgname}/uifontmetrics) = %{version}
Provides:       crate(%{pkgname}/uimenuleaf) = %{version}
Provides:       crate(%{pkgname}/uinibloading) = %{version}
Provides:       crate(%{pkgname}/uisearchdisplaycontroller) = %{version}
Provides:       crate(%{pkgname}/uisearchtab) = %{version}
Provides:       crate(%{pkgname}/uismartreplysuggestion) = %{version}
Provides:       crate(%{pkgname}/uistoryboardpopoversegue) = %{version}
Provides:       crate(%{pkgname}/uistoryboardsegue) = %{version}
Provides:       crate(%{pkgname}/uistringdrawing) = %{version}
Provides:       crate(%{pkgname}/uitab) = %{version}
Provides:       crate(%{pkgname}/uitooltipinteraction) = %{version}
Provides:       crate(%{pkgname}/uitrait) = %{version}

%description -n %{name}+uiaccessibilityelement
This metapackage enables feature "UIAccessibilityElement" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAccessibilityIdentification", "UIActivityItemsConfigurationReading_ShareSheet", "UIContextualAction", "UIDocumentViewControllerLaunchOptions", "UIFindSession", "UIFontMetrics", "UIMenuLeaf", "UINibLoading", "UISearchDisplayController", "UISearchTab", "UISmartReplySuggestion", "UIStoryboardPopoverSegue", "UIStoryboardSegue", "UIStringDrawing", "UITab", "UIToolTipInteraction", and "UITrait" features.

%package     -n %{name}+uiaction
Summary:        Bindings to the UIKit framework - feature "UIAction" and 9 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaction) = %{version}
Provides:       crate(%{pkgname}/uiactionsheet) = %{version}
Provides:       crate(%{pkgname}/uialertview) = %{version}
Provides:       crate(%{pkgname}/uicollectionviewcell) = %{version}
Provides:       crate(%{pkgname}/uicollectionviewtransitionlayout) = %{version}
Provides:       crate(%{pkgname}/uicolorwell) = %{version}
Provides:       crate(%{pkgname}/uicontentunavailableconfigurationstate) = %{version}
Provides:       crate(%{pkgname}/uiswitch) = %{version}
Provides:       crate(%{pkgname}/uitableviewheaderfooterview) = %{version}
Provides:       crate(%{pkgname}/uiwindowsceneactivationaction) = %{version}

%description -n %{name}+uiaction
This metapackage enables feature "UIAction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIActionSheet", "UIAlertView", "UICollectionViewCell", "UICollectionViewTransitionLayout", "UIColorWell", "UIContentUnavailableConfigurationState", "UISwitch", "UITableViewHeaderFooterView", and "UIWindowSceneActivationAction" features.

%package     -n %{name}+uiactivity
Summary:        Bindings to the UIKit framework - feature "UIActivity" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivity) = %{version}
Provides:       crate(%{pkgname}/uifindinteraction) = %{version}
Provides:       crate(%{pkgname}/uilocalizedindexedcollation) = %{version}
Provides:       crate(%{pkgname}/uimenubuilder) = %{version}
Provides:       crate(%{pkgname}/uisheetpresentationcontroller) = %{version}
Provides:       crate(%{pkgname}/uitabgroup) = %{version}

%description -n %{name}+uiactivity
This metapackage enables feature "UIActivity" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIFindInteraction", "UILocalizedIndexedCollation", "UIMenuBuilder", "UISheetPresentationController", and "UITabGroup" features.

%package     -n %{name}+uiactivitycollaborationmoderestriction
Summary:        Bindings to the UIKit framework - feature "UIActivityCollaborationModeRestriction" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivitycollaborationmoderestriction) = %{version}
Provides:       crate(%{pkgname}/uieventattribution) = %{version}

%description -n %{name}+uiactivitycollaborationmoderestriction
This metapackage enables feature "UIActivityCollaborationModeRestriction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIEventAttribution" feature.

%package     -n %{name}+uiactivityitemprovider
Summary:        Bindings to the UIKit framework - feature "UIActivityItemProvider"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivityitemprovider) = %{version}

%description -n %{name}+uiactivityitemprovider
This metapackage enables feature "UIActivityItemProvider" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiactivityitemsconfiguration
Summary:        Bindings to the UIKit framework - feature "UIActivityItemsConfiguration" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivityitemsconfiguration) = %{version}
Provides:       crate(%{pkgname}/uiactivityitemsconfigurationreading) = %{version}

%description -n %{name}+uiactivityitemsconfiguration
This metapackage enables feature "UIActivityItemsConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIActivityItemsConfigurationReading" feature.

%package     -n %{name}+uiactivityviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIActivityViewController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivityviewcontroller) = %{version}

%description -n %{name}+uiactivityviewcontroller
This metapackage enables feature "UIActivityViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uialertcontroller
Summary:        Bindings to the UIKit framework - feature "UIAlertController" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uialertcontroller) = %{version}
Provides:       crate(%{pkgname}/uinavigationcontroller) = %{version}
Provides:       crate(%{pkgname}/uisearchcontroller) = %{version}
Provides:       crate(%{pkgname}/uisplitviewcontroller) = %{version}

%description -n %{name}+uialertcontroller
This metapackage enables feature "UIAlertController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UINavigationController", "UISearchController", and "UISplitViewController" features.

%package     -n %{name}+uiappearance
Summary:        Bindings to the UIKit framework - feature "UIAppearance" and 14 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Provides:       crate(%{pkgname}/uiappearance) = %{version}
Provides:       crate(%{pkgname}/uiattachmentbehavior) = %{version}
Provides:       crate(%{pkgname}/uidraginteraction) = %{version}
Provides:       crate(%{pkgname}/uidynamicbehavior) = %{version}
Provides:       crate(%{pkgname}/uidynamicitembehavior) = %{version}
Provides:       crate(%{pkgname}/uigravitybehavior) = %{version}
Provides:       crate(%{pkgname}/uiinteraction) = %{version}
Provides:       crate(%{pkgname}/uipopovercontroller) = %{version}
Provides:       crate(%{pkgname}/uipopoverpresentationcontroller) = %{version}
Provides:       crate(%{pkgname}/uiprintpaper) = %{version}
Provides:       crate(%{pkgname}/uipushbehavior) = %{version}
Provides:       crate(%{pkgname}/uiswipeactionsconfiguration) = %{version}
Provides:       crate(%{pkgname}/uitextinteraction) = %{version}
Provides:       crate(%{pkgname}/uitextselectiondisplayinteraction) = %{version}
Provides:       crate(%{pkgname}/uitextselectionhighlightview) = %{version}

%description -n %{name}+uiappearance
This metapackage enables feature "UIAppearance" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAttachmentBehavior", "UIDragInteraction", "UIDynamicBehavior", "UIDynamicItemBehavior", "UIGravityBehavior", "UIInteraction", "UIPopoverController", "UIPopoverPresentationController", "UIPrintPaper", "UIPushBehavior", "UISwipeActionsConfiguration", "UITextInteraction", "UITextSelectionDisplayInteraction", and "UITextSelectionHighlightView" features.

%package     -n %{name}+uiapplication
Summary:        Bindings to the UIKit framework - feature "UIApplication"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiapplication) = %{version}

%description -n %{name}+uiapplication
This metapackage enables feature "UIApplication" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiapplicationshortcutitem
Summary:        Bindings to the UIKit framework - feature "UIApplicationShortcutItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiapplicationshortcutitem) = %{version}

%description -n %{name}+uiapplicationshortcutitem
This metapackage enables feature "UIApplicationShortcutItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uibackgroundconfiguration
Summary:        Bindings to the UIKit framework - feature "UIBackgroundConfiguration" and 42 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uibackgroundconfiguration) = %{version}
Provides:       crate(%{pkgname}/uiblureffect) = %{version}
Provides:       crate(%{pkgname}/uicontentconfiguration) = %{version}
Provides:       crate(%{pkgname}/uicontentunavailablebuttonproperties) = %{version}
Provides:       crate(%{pkgname}/uicontentunavailableimageproperties) = %{version}
Provides:       crate(%{pkgname}/uicontentunavailabletextproperties) = %{version}
Provides:       crate(%{pkgname}/uicontextmenuinteraction) = %{version}
Provides:       crate(%{pkgname}/uicornerconfiguration) = %{version}
Provides:       crate(%{pkgname}/uicornerradius) = %{version}
Provides:       crate(%{pkgname}/uidragpreview) = %{version}
Provides:       crate(%{pkgname}/uifocuseffect) = %{version}
Provides:       crate(%{pkgname}/uifocusmovementhint) = %{version}
Provides:       crate(%{pkgname}/uiglasseffect) = %{version}
Provides:       crate(%{pkgname}/uigraphicsrenderer) = %{version}
Provides:       crate(%{pkgname}/uihovereffect) = %{version}
Provides:       crate(%{pkgname}/uihovereffectlayer) = %{version}
Provides:       crate(%{pkgname}/uihoverstyle) = %{version}
Provides:       crate(%{pkgname}/uikeyboardlayoutguide) = %{version}
Provides:       crate(%{pkgname}/uilistcontentimageproperties) = %{version}
Provides:       crate(%{pkgname}/uilistcontenttextproperties) = %{version}
Provides:       crate(%{pkgname}/uilistseparatorconfiguration) = %{version}
Provides:       crate(%{pkgname}/uimainmenusystem) = %{version}
Provides:       crate(%{pkgname}/uimenudisplaypreferences) = %{version}
Provides:       crate(%{pkgname}/uipointeraccessory) = %{version}
Provides:       crate(%{pkgname}/uipointerregion) = %{version}
Provides:       crate(%{pkgname}/uiregion) = %{version}
Provides:       crate(%{pkgname}/uiscenedestructioncondition) = %{version}
Provides:       crate(%{pkgname}/uishadowproperties) = %{version}
Provides:       crate(%{pkgname}/uishape) = %{version}
Provides:       crate(%{pkgname}/uisymbolcontenttransition) = %{version}
Provides:       crate(%{pkgname}/uitargeteddragpreview) = %{version}
Provides:       crate(%{pkgname}/uitargetedpreview) = %{version}
Provides:       crate(%{pkgname}/uitextdropproposal) = %{version}
Provides:       crate(%{pkgname}/uitimingcurveprovider) = %{version}
Provides:       crate(%{pkgname}/uivibrancyeffect) = %{version}
Provides:       crate(%{pkgname}/uivisualeffect) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenegeometry) = %{version}
Provides:       crate(%{pkgname}/uiwindowsceneplacement) = %{version}
Provides:       crate(%{pkgname}/uiwindowsceneprominentplacement) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenepushplacement) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenereplaceplacement) = %{version}
Provides:       crate(%{pkgname}/uiwindowscenestandardplacement) = %{version}
Provides:       crate(%{pkgname}/uizoomtransitionoptions) = %{version}

%description -n %{name}+uibackgroundconfiguration
This metapackage enables feature "UIBackgroundConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIBlurEffect", "UIContentConfiguration", "UIContentUnavailableButtonProperties", "UIContentUnavailableImageProperties", "UIContentUnavailableTextProperties", "UIContextMenuInteraction", "UICornerConfiguration", "UICornerRadius", "UIDragPreview", "UIFocusEffect", "UIFocusMovementHint", "UIGlassEffect", "UIGraphicsRenderer", "UIHoverEffect", "UIHoverEffectLayer", "UIHoverStyle", "UIKeyboardLayoutGuide", "UIListContentImageProperties", "UIListContentTextProperties", "UIListSeparatorConfiguration", "UIMainMenuSystem", "UIMenuDisplayPreferences", "UIPointerAccessory", "UIPointerRegion", "UIRegion", "UISceneDestructionCondition", "UIShadowProperties", "UIShape", "UISymbolContentTransition", "UITargetedDragPreview", "UITargetedPreview", "UITextDropProposal", "UITimingCurveProvider", "UIVibrancyEffect", "UIVisualEffect", "UIWindowSceneGeometry", "UIWindowScenePlacement", "UIWindowSceneProminentPlacement", "UIWindowScenePushPlacement", "UIWindowSceneReplacePlacement", "UIWindowSceneStandardPlacement", and "UIZoomTransitionOptions" features.

%package     -n %{name}+uibarbuttonitem
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitem) = %{version}

%description -n %{name}+uibarbuttonitem
This metapackage enables feature "UIBarButtonItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uibarbuttonitemappearance
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItemAppearance" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitemappearance) = %{version}
Provides:       crate(%{pkgname}/uibaritem) = %{version}
Provides:       crate(%{pkgname}/uinavigationbarappearance) = %{version}
Provides:       crate(%{pkgname}/uitabbarappearance) = %{version}
Provides:       crate(%{pkgname}/uitabbaritem) = %{version}

%description -n %{name}+uibarbuttonitemappearance
This metapackage enables feature "UIBarButtonItemAppearance" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIBarItem", "UINavigationBarAppearance", "UITabBarAppearance", and "UITabBarItem" features.

%package     -n %{name}+uibarbuttonitembadge
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItemBadge" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitembadge) = %{version}
Provides:       crate(%{pkgname}/uiconfigurationstate) = %{version}
Provides:       crate(%{pkgname}/uikey) = %{version}
Provides:       crate(%{pkgname}/uilayoutguide) = %{version}
Provides:       crate(%{pkgname}/uisceneconfiguration) = %{version}

%description -n %{name}+uibarbuttonitembadge
This metapackage enables feature "UIBarButtonItemBadge" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIConfigurationState", "UIKey", "UILayoutGuide", and "UISceneConfiguration" features.

%package     -n %{name}+uibarbuttonitemgroup
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItemGroup" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitemgroup) = %{version}
Provides:       crate(%{pkgname}/uicellaccessory) = %{version}
Provides:       crate(%{pkgname}/uideferredmenuelement) = %{version}
Provides:       crate(%{pkgname}/uikeycommand) = %{version}
Provides:       crate(%{pkgname}/uitraitcollection) = %{version}

%description -n %{name}+uibarbuttonitemgroup
This metapackage enables feature "UIBarButtonItemGroup" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICellAccessory", "UIDeferredMenuElement", "UIKeyCommand", and "UITraitCollection" features.

%package     -n %{name}+uibutton
Summary:        Bindings to the UIKit framework - feature "UIButton" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibutton) = %{version}
Provides:       crate(%{pkgname}/uilabel) = %{version}
Provides:       crate(%{pkgname}/uilistcontentconfiguration) = %{version}
Provides:       crate(%{pkgname}/uipickerview) = %{version}

%description -n %{name}+uibutton
This metapackage enables feature "UIButton" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UILabel", "UIListContentConfiguration", and "UIPickerView" features.

%package     -n %{name}+uibuttonconfiguration
Summary:        Bindings to the UIKit framework - feature "UIButtonConfiguration" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibuttonconfiguration) = %{version}
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerformattingstyle) = %{version}

%description -n %{name}+uibuttonconfiguration
This metapackage enables feature "UIButtonConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UITextFormattingViewControllerFormattingStyle" feature.

%package     -n %{name}+uicalendarselectionmultidate
Summary:        Bindings to the UIKit framework - feature "UICalendarSelectionMultiDate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Provides:       crate(%{pkgname}/uicalendarselectionmultidate) = %{version}

%description -n %{name}+uicalendarselectionmultidate
This metapackage enables feature "UICalendarSelectionMultiDate" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicalendarselectionsingledate
Summary:        Bindings to the UIKit framework - feature "UICalendarSelectionSingleDate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Provides:       crate(%{pkgname}/uicalendarselectionsingledate) = %{version}
Provides:       crate(%{pkgname}/uicalendarselectionweekofyear) = %{version}

%description -n %{name}+uicalendarselectionsingledate
This metapackage enables feature "UICalendarSelectionSingleDate" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICalendarSelectionWeekOfYear" feature.

%package     -n %{name}+uicalendarview
Summary:        Bindings to the UIKit framework - feature "UICalendarView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdateinterval) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/uicalendarview) = %{version}

%description -n %{name}+uicalendarview
This metapackage enables feature "UICalendarView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicloudsharingcontroller
Summary:        Bindings to the UIKit framework - feature "UICloudSharingController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicloudsharingcontroller) = %{version}

%description -n %{name}+uicloudsharingcontroller
This metapackage enables feature "UICloudSharingController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionlayoutlist
Summary:        Bindings to the UIKit framework - feature "UICollectionLayoutList"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionlayoutlist) = %{version}

%description -n %{name}+uicollectionlayoutlist
This metapackage enables feature "UICollectionLayoutList" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionview
Summary:        Bindings to the UIKit framework - feature "UICollectionView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionview) = %{version}

%description -n %{name}+uicollectionview
This metapackage enables feature "UICollectionView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewcompositionallayout
Summary:        Bindings to the UIKit framework - feature "UICollectionViewCompositionalLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewcompositionallayout) = %{version}

%description -n %{name}+uicollectionviewcompositionallayout
This metapackage enables feature "UICollectionViewCompositionalLayout" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewcontroller
Summary:        Bindings to the UIKit framework - feature "UICollectionViewController" and 7 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uicolorpickerviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uidocumentviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uifontpickerviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uireferencelibraryviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uisearchcontainerviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uitableviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uitextformattingviewcontroller) = %{version}

%description -n %{name}+uicollectionviewcontroller
This metapackage enables feature "UICollectionViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIColorPickerViewController", "UIDocumentViewController", "UIFontPickerViewController", "UIReferenceLibraryViewController", "UISearchContainerViewController", "UITableViewController", and "UITextFormattingViewController" features.

%package     -n %{name}+uicollectionviewflowlayout
Summary:        Bindings to the UIKit framework - feature "UICollectionViewFlowLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewflowlayout) = %{version}

%description -n %{name}+uicollectionviewflowlayout
This metapackage enables feature "UICollectionViewFlowLayout" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewitemregistration
Summary:        Bindings to the UIKit framework - feature "UICollectionViewItemRegistration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewitemregistration) = %{version}

%description -n %{name}+uicollectionviewitemregistration
This metapackage enables feature "UICollectionViewItemRegistration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewlayout
Summary:        Bindings to the UIKit framework - feature "UICollectionViewLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewlayout) = %{version}

%description -n %{name}+uicollectionviewlayout
This metapackage enables feature "UICollectionViewLayout" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollisionbehavior
Summary:        Bindings to the UIKit framework - feature "UICollisionBehavior"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uicollisionbehavior) = %{version}

%description -n %{name}+uicollisionbehavior
This metapackage enables feature "UICollisionBehavior" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicolor
Summary:        Bindings to the UIKit framework - feature "UIColor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicolor) = %{version}

%description -n %{name}+uicolor
This metapackage enables feature "UIColor" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicommand
Summary:        Bindings to the UIKit framework - feature "UICommand" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicommand) = %{version}
Provides:       crate(%{pkgname}/uimenu) = %{version}

%description -n %{name}+uicommand
This metapackage enables feature "UICommand" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIMenu" feature.

%package     -n %{name}+uicontentsizecategory
Summary:        Bindings to the UIKit framework - feature "UIContentSizeCategory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicontentsizecategory) = %{version}

%description -n %{name}+uicontentsizecategory
This metapackage enables feature "UIContentSizeCategory" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicontentunavailableconfiguration
Summary:        Bindings to the UIKit framework - feature "UIContentUnavailableConfiguration" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicontentunavailableconfiguration) = %{version}
Provides:       crate(%{pkgname}/uiprintformatter) = %{version}

%description -n %{name}+uicontentunavailableconfiguration
This metapackage enables feature "UIContentUnavailableConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPrintFormatter" feature.

%package     -n %{name}+uicontextmenuconfiguration
Summary:        Bindings to the UIKit framework - feature "UIContextMenuConfiguration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uicontextmenuconfiguration) = %{version}

%description -n %{name}+uicontextmenuconfiguration
This metapackage enables feature "UIContextMenuConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicontrol
Summary:        Bindings to the UIKit framework - feature "UIControl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicontrol) = %{version}

%description -n %{name}+uicontrol
This metapackage enables feature "UIControl" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiconversationcontext
Summary:        Bindings to the UIKit framework - feature "UIConversationContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspersonnamecomponents) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiconversationcontext) = %{version}

%description -n %{name}+uiconversationcontext
This metapackage enables feature "UIConversationContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiconversationentry
Summary:        Bindings to the UIKit framework - feature "UIConversationEntry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiconversationentry) = %{version}

%description -n %{name}+uiconversationentry
This metapackage enables feature "UIConversationEntry" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidatepicker
Summary:        Bindings to the UIKit framework - feature "UIDatePicker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/uidatepicker) = %{version}

%description -n %{name}+uidatepicker
This metapackage enables feature "UIDatePicker" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidevice
Summary:        Bindings to the UIKit framework - feature "UIDevice"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/uidevice) = %{version}

%description -n %{name}+uidevice
This metapackage enables feature "UIDevice" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidiffabledatasource
Summary:        Bindings to the UIKit framework - feature "UIDiffableDataSource"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsorderedcollectiondifference) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uidiffabledatasource) = %{version}

%description -n %{name}+uidiffabledatasource
This metapackage enables feature "UIDiffableDataSource" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocument
Summary:        Bindings to the UIKit framework - feature "UIDocument"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilepresenter) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsundomanager) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uidocument) = %{version}

%description -n %{name}+uidocument
This metapackage enables feature "UIDocument" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentbrowseraction
Summary:        Bindings to the UIKit framework - feature "UIDocumentBrowserAction"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentbrowseraction) = %{version}

%description -n %{name}+uidocumentbrowseraction
This metapackage enables feature "UIDocumentBrowserAction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentbrowserviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIDocumentBrowserViewController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentbrowserviewcontroller) = %{version}

%description -n %{name}+uidocumentbrowserviewcontroller
This metapackage enables feature "UIDocumentBrowserViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentinteractioncontroller
Summary:        Bindings to the UIKit framework - feature "UIDocumentInteractionController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentinteractioncontroller) = %{version}

%description -n %{name}+uidocumentinteractioncontroller
This metapackage enables feature "UIDocumentInteractionController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentmenuviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIDocumentMenuViewController" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentmenuviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uidocumentpickerextensionviewcontroller) = %{version}
Provides:       crate(%{pkgname}/uidocumentpickerviewcontroller) = %{version}

%description -n %{name}+uidocumentmenuviewcontroller
This metapackage enables feature "UIDocumentMenuViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIDocumentPickerExtensionViewController", and "UIDocumentPickerViewController" features.

%package     -n %{name}+uidocumentproperties
Summary:        Bindings to the UIKit framework - feature "UIDocumentProperties"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentproperties) = %{version}

%description -n %{name}+uidocumentproperties
This metapackage enables feature "UIDocumentProperties" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidragitem
Summary:        Bindings to the UIKit framework - feature "UIDragItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Provides:       crate(%{pkgname}/uidragitem) = %{version}

%description -n %{name}+uidragitem
This metapackage enables feature "UIDragItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidragpreviewparameters
Summary:        Bindings to the UIKit framework - feature "UIDragPreviewParameters" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uidragpreviewparameters) = %{version}
Provides:       crate(%{pkgname}/uipreviewparameters) = %{version}

%description -n %{name}+uidragpreviewparameters
This metapackage enables feature "UIDragPreviewParameters" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPreviewParameters" feature.

%package     -n %{name}+uidragsession
Summary:        Bindings to the UIKit framework - feature "UIDragSession"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uidragsession) = %{version}

%description -n %{name}+uidragsession
This metapackage enables feature "UIDragSession" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidropinteraction
Summary:        Bindings to the UIKit framework - feature "UIDropInteraction"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uidropinteraction) = %{version}

%description -n %{name}+uidropinteraction
This metapackage enables feature "UIDropInteraction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidynamicanimator
Summary:        Bindings to the UIKit framework - feature "UIDynamicAnimator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uidynamicanimator) = %{version}

%description -n %{name}+uidynamicanimator
This metapackage enables feature "UIDynamicAnimator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uieditmenuinteraction
Summary:        Bindings to the UIKit framework - feature "UIEditMenuInteraction" and 6 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uieditmenuinteraction) = %{version}
Provides:       crate(%{pkgname}/uifocusguide) = %{version}
Provides:       crate(%{pkgname}/uiindirectscribbleinteraction) = %{version}
Provides:       crate(%{pkgname}/uipointerstyle) = %{version}
Provides:       crate(%{pkgname}/uitabsidebaritem) = %{version}
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerconfiguration) = %{version}
Provides:       crate(%{pkgname}/uitrackinglayoutguide) = %{version}

%description -n %{name}+uieditmenuinteraction
This metapackage enables feature "UIEditMenuInteraction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIFocusGuide", "UIIndirectScribbleInteraction", "UIPointerStyle", "UITabSidebarItem", "UITextFormattingViewControllerConfiguration", and "UITrackingLayoutGuide" features.

%package     -n %{name}+uievent
Summary:        Bindings to the UIKit framework - feature "UIEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uievent) = %{version}

%description -n %{name}+uievent
This metapackage enables feature "UIEvent" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uifieldbehavior
Summary:        Bindings to the UIKit framework - feature "UIFieldBehavior" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Provides:       crate(%{pkgname}/uifieldbehavior) = %{version}
Provides:       crate(%{pkgname}/uipress) = %{version}

%description -n %{name}+uifieldbehavior
This metapackage enables feature "UIFieldBehavior" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPress" feature.

%package     -n %{name}+uifocus
Summary:        Bindings to the UIKit framework - feature "UIFocus"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uifocus) = %{version}

%description -n %{name}+uifocus
This metapackage enables feature "UIFocus" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uifocussystem-uikitadditions
Summary:        Bindings to the UIKit framework - feature "UIFocusSystem_UIKitAdditions" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uifocussystem-uikitadditions) = %{version}
Provides:       crate(%{pkgname}/uitextdragurlpreviews) = %{version}

%description -n %{name}+uifocussystem-uikitadditions
This metapackage enables feature "UIFocusSystem_UIKitAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UITextDragURLPreviews" feature.

%package     -n %{name}+uifontdescriptor
Summary:        Bindings to the UIKit framework - feature "UIFontDescriptor" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uifontdescriptor) = %{version}
Provides:       crate(%{pkgname}/uiusernotificationsettings) = %{version}

%description -n %{name}+uifontdescriptor
This metapackage enables feature "UIFontDescriptor" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIUserNotificationSettings" feature.

%package     -n %{name}+uifontpickerviewcontrollerconfiguration
Summary:        Bindings to the UIKit framework - feature "UIFontPickerViewControllerConfiguration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uifontpickerviewcontrollerconfiguration) = %{version}

%description -n %{name}+uifontpickerviewcontrollerconfiguration
This metapackage enables feature "UIFontPickerViewControllerConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigeometry
Summary:        Bindings to the UIKit framework - feature "UIGeometry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uigeometry) = %{version}

%description -n %{name}+uigeometry
This metapackage enables feature "UIGeometry" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UIGestureRecognizer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uigesturerecognizer) = %{version}

%description -n %{name}+uigesturerecognizer
This metapackage enables feature "UIGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigesturerecognizersubclass
Summary:        Bindings to the UIKit framework - feature "UIGestureRecognizerSubclass" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uigesturerecognizersubclass) = %{version}
Provides:       crate(%{pkgname}/uipressesevent) = %{version}

%description -n %{name}+uigesturerecognizersubclass
This metapackage enables feature "UIGestureRecognizerSubclass" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPressesEvent" feature.

%package     -n %{name}+uigraphics
Summary:        Bindings to the UIKit framework - feature "UIGraphics"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphics) = %{version}

%description -n %{name}+uigraphics
This metapackage enables feature "UIGraphics" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigraphicsimagerenderer
Summary:        Bindings to the UIKit framework - feature "UIGraphicsImageRenderer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphicsimagerenderer) = %{version}

%description -n %{name}+uigraphicsimagerenderer
This metapackage enables feature "UIGraphicsImageRenderer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigraphicspdfrenderer
Summary:        Bindings to the UIKit framework - feature "UIGraphicsPDFRenderer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphicspdfrenderer) = %{version}

%description -n %{name}+uigraphicspdfrenderer
This metapackage enables feature "UIGraphicsPDFRenderer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigraphicsrenderersubclass
Summary:        Bindings to the UIKit framework - feature "UIGraphicsRendererSubclass" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphicsrenderersubclass) = %{version}
Provides:       crate(%{pkgname}/uiprinterpickercontroller) = %{version}
Provides:       crate(%{pkgname}/uiwindowsceneactivationinteraction) = %{version}

%description -n %{name}+uigraphicsrenderersubclass
This metapackage enables feature "UIGraphicsRendererSubclass" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPrinterPickerController", and "UIWindowSceneActivationInteraction" features.

%package     -n %{name}+uiguidedaccess
Summary:        Bindings to the UIKit framework - feature "UIGuidedAccess"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiguidedaccess) = %{version}

%description -n %{name}+uiguidedaccess
This metapackage enables feature "UIGuidedAccess" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uihovergesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UIHoverGestureRecognizer" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Provides:       crate(%{pkgname}/uihovergesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/uipinchgesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/uirotationgesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/uiscreenedgepangesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/uitapgesturerecognizer) = %{version}

%description -n %{name}+uihovergesturerecognizer
This metapackage enables feature "UIHoverGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPinchGestureRecognizer", "UIRotationGestureRecognizer", "UIScreenEdgePanGestureRecognizer", and "UITapGestureRecognizer" features.

%package     -n %{name}+uiimage
Summary:        Bindings to the UIKit framework - feature "UIImage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiimage) = %{version}

%description -n %{name}+uiimage
This metapackage enables feature "UIImage" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimageconfiguration
Summary:        Bindings to the UIKit framework - feature "UIImageConfiguration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uiimageconfiguration) = %{version}

%description -n %{name}+uiimageconfiguration
This metapackage enables feature "UIImageConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimagepickercontroller
Summary:        Bindings to the UIKit framework - feature "UIImagePickerController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uiimagepickercontroller) = %{version}

%description -n %{name}+uiimagepickercontroller
This metapackage enables feature "UIImagePickerController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimagereader
Summary:        Bindings to the UIKit framework - feature "UIImageReader"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiimagereader) = %{version}

%description -n %{name}+uiimagereader
This metapackage enables feature "UIImageReader" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimagesymbolconfiguration
Summary:        Bindings to the UIKit framework - feature "UIImageSymbolConfiguration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiimagesymbolconfiguration) = %{version}

%description -n %{name}+uiimagesymbolconfiguration
This metapackage enables feature "UIImageSymbolConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimageview
Summary:        Bindings to the UIKit framework - feature "UIImageView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uiimageview) = %{version}

%description -n %{name}+uiimageview
This metapackage enables feature "UIImageView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiinputviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIInputViewController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/uiinputviewcontroller) = %{version}

%description -n %{name}+uiinputviewcontroller
This metapackage enables feature "UIInputViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uilargecontentviewer
Summary:        Bindings to the UIKit framework - feature "UILargeContentViewer" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uilargecontentviewer) = %{version}
Provides:       crate(%{pkgname}/uipointerlockstate) = %{version}
Provides:       crate(%{pkgname}/uiscenesystemprotectionmanager) = %{version}

%description -n %{name}+uilargecontentviewer
This metapackage enables feature "UILargeContentViewer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPointerLockState", and "UISceneSystemProtectionManager" features.

%package     -n %{name}+uilocalnotification
Summary:        Bindings to the UIKit framework - feature "UILocalNotification"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/uilocalnotification) = %{version}

%description -n %{name}+uilocalnotification
This metapackage enables feature "UILocalNotification" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uilongpressgesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UILongPressGestureRecognizer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Provides:       crate(%{pkgname}/uilongpressgesturerecognizer) = %{version}

%description -n %{name}+uilongpressgesturerecognizer
This metapackage enables feature "UILongPressGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uimailconversationcontext
Summary:        Bindings to the UIKit framework - feature "UIMailConversationContext" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uimailconversationcontext) = %{version}
Provides:       crate(%{pkgname}/uimailconversationentry) = %{version}

%description -n %{name}+uimailconversationcontext
This metapackage enables feature "UIMailConversationContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIMailConversationEntry" feature.

%package     -n %{name}+uimanageddocument
Summary:        Bindings to the UIKit framework - feature "UIManagedDocument"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilepresenter) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uimanageddocument) = %{version}

%description -n %{name}+uimanageddocument
This metapackage enables feature "UIManagedDocument" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uimenucontroller
Summary:        Bindings to the UIKit framework - feature "UIMenuController" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uimenucontroller) = %{version}
Provides:       crate(%{pkgname}/uiscreen) = %{version}

%description -n %{name}+uimenucontroller
This metapackage enables feature "UIMenuController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIScreen" feature.

%package     -n %{name}+uimotioneffect
Summary:        Bindings to the UIKit framework - feature "UIMotionEffect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uimotioneffect) = %{version}

%description -n %{name}+uimotioneffect
This metapackage enables feature "UIMotionEffect" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uinavigationitem
Summary:        Bindings to the UIKit framework - feature "UINavigationItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uinavigationitem) = %{version}

%description -n %{name}+uinavigationitem
This metapackage enables feature "UINavigationItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uinib
Summary:        Bindings to the UIKit framework - feature "UINib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uinib) = %{version}

%description -n %{name}+uinib
This metapackage enables feature "UINib" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiopenurlcontext
Summary:        Bindings to the UIKit framework - feature "UIOpenURLContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiopenurlcontext) = %{version}

%description -n %{name}+uiopenurlcontext
This metapackage enables feature "UIOpenURLContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipageviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIPageViewController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uipageviewcontroller) = %{version}

%description -n %{name}+uipageviewcontroller
This metapackage enables feature "UIPageViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipangesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UIPanGestureRecognizer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Provides:       crate(%{pkgname}/uipangesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/uiswipegesturerecognizer) = %{version}

%description -n %{name}+uipangesturerecognizer
This metapackage enables feature "UIPanGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UISwipeGestureRecognizer" feature.

%package     -n %{name}+uipasteconfiguration
Summary:        Bindings to the UIKit framework - feature "UIPasteConfiguration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uipasteconfiguration) = %{version}

%description -n %{name}+uipasteconfiguration
This metapackage enables feature "UIPasteConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipasteconfigurationsupporting
Summary:        Bindings to the UIKit framework - feature "UIPasteConfigurationSupporting"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Provides:       crate(%{pkgname}/uipasteconfigurationsupporting) = %{version}

%description -n %{name}+uipasteconfigurationsupporting
This metapackage enables feature "UIPasteConfigurationSupporting" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipasteboard
Summary:        Bindings to the UIKit framework - feature "UIPasteboard"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uipasteboard) = %{version}

%description -n %{name}+uipasteboard
This metapackage enables feature "UIPasteboard" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprinterror
Summary:        Bindings to the UIKit framework - feature "UIPrintError" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiprinterror) = %{version}
Provides:       crate(%{pkgname}/uiscenedefinitions) = %{version}

%description -n %{name}+uiprinterror
This metapackage enables feature "UIPrintError" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UISceneDefinitions" feature.

%package     -n %{name}+uiprintinfo
Summary:        Bindings to the UIKit framework - feature "UIPrintInfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiprintinfo) = %{version}

%description -n %{name}+uiprintinfo
This metapackage enables feature "UIPrintInfo" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprintinteractioncontroller
Summary:        Bindings to the UIKit framework - feature "UIPrintInteractionController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiprintinteractioncontroller) = %{version}

%description -n %{name}+uiprintinteractioncontroller
This metapackage enables feature "UIPrintInteractionController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprintserviceextension
Summary:        Bindings to the UIKit framework - feature "UIPrintServiceExtension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiprintserviceextension) = %{version}

%description -n %{name}+uiprintserviceextension
This metapackage enables feature "UIPrintServiceExtension" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprinter
Summary:        Bindings to the UIKit framework - feature "UIPrinter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiprinter) = %{version}

%description -n %{name}+uiprinter
This metapackage enables feature "UIPrinter" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprogressview
Summary:        Bindings to the UIKit framework - feature "UIProgressView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uiprogressview) = %{version}

%description -n %{name}+uiprogressview
This metapackage enables feature "UIProgressView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uirefreshcontrol
Summary:        Bindings to the UIKit framework - feature "UIRefreshControl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uirefreshcontrol) = %{version}

%description -n %{name}+uirefreshcontrol
This metapackage enables feature "UIRefreshControl" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiresponder
Summary:        Bindings to the UIKit framework - feature "UIResponder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsundomanager) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiresponder) = %{version}

%description -n %{name}+uiresponder
This metapackage enables feature "UIResponder" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscene
Summary:        Bindings to the UIKit framework - feature "UIScene"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiscene) = %{version}

%description -n %{name}+uiscene
This metapackage enables feature "UIScene" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisceneactivationconditions
Summary:        Bindings to the UIKit framework - feature "UISceneActivationConditions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uisceneactivationconditions) = %{version}

%description -n %{name}+uisceneactivationconditions
This metapackage enables feature "UISceneActivationConditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisceneoptions
Summary:        Bindings to the UIKit framework - feature "UISceneOptions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uisceneoptions) = %{version}

%description -n %{name}+uisceneoptions
This metapackage enables feature "UISceneOptions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscenesession
Summary:        Bindings to the UIKit framework - feature "UISceneSession"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/uisceneconfiguration) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiscenesession) = %{version}

%description -n %{name}+uiscenesession
This metapackage enables feature "UISceneSession" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscenesessionactivationrequest
Summary:        Bindings to the UIKit framework - feature "UISceneSessionActivationRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiscenesessionactivationrequest) = %{version}

%description -n %{name}+uiscenesessionactivationrequest
This metapackage enables feature "UISceneSessionActivationRequest" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscreenshotservice
Summary:        Bindings to the UIKit framework - feature "UIScreenshotService"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Provides:       crate(%{pkgname}/uiscreenshotservice) = %{version}

%description -n %{name}+uiscreenshotservice
This metapackage enables feature "UIScreenshotService" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscrollview
Summary:        Bindings to the UIKit framework - feature "UIScrollView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uiscrollview) = %{version}

%description -n %{name}+uiscrollview
This metapackage enables feature "UIScrollView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisearchbar
Summary:        Bindings to the UIKit framework - feature "UISearchBar"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uisearchbar) = %{version}

%description -n %{name}+uisearchbar
This metapackage enables feature "UISearchBar" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisearchtextfield
Summary:        Bindings to the UIKit framework - feature "UISearchTextField"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uisearchtextfield) = %{version}

%description -n %{name}+uisearchtextfield
This metapackage enables feature "UISearchTextField" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uistaterestoration
Summary:        Bindings to the UIKit framework - feature "UIStateRestoration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uistaterestoration) = %{version}

%description -n %{name}+uistaterestoration
This metapackage enables feature "UIStateRestoration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uistoryboard
Summary:        Bindings to the UIKit framework - feature "UIStoryboard"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uistoryboard) = %{version}

%description -n %{name}+uistoryboard
This metapackage enables feature "UIStoryboard" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitabbarcontroller
Summary:        Bindings to the UIKit framework - feature "UITabBarController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitabbarcontroller) = %{version}

%description -n %{name}+uitabbarcontroller
This metapackage enables feature "UITabBarController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitabbarcontrollersidebar
Summary:        Bindings to the UIKit framework - feature "UITabBarControllerSidebar"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uitabbarcontrollersidebar) = %{version}

%description -n %{name}+uitabbarcontrollersidebar
This metapackage enables feature "UITabBarControllerSidebar" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitableview
Summary:        Bindings to the UIKit framework - feature "UITableView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitableview) = %{version}

%description -n %{name}+uitableview
This metapackage enables feature "UITableView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextchecker
Summary:        Bindings to the UIKit framework - feature "UITextChecker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextchecker) = %{version}

%description -n %{name}+uitextchecker
This metapackage enables feature "UITextChecker" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextdragpreviewrenderer
Summary:        Bindings to the UIKit framework - feature "UITextDragPreviewRenderer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Provides:       crate(%{pkgname}/uitextdragpreviewrenderer) = %{version}

%description -n %{name}+uitextdragpreviewrenderer
This metapackage enables feature "UITextDragPreviewRenderer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextdragging
Summary:        Bindings to the UIKit framework - feature "UITextDragging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Provides:       crate(%{pkgname}/uitextdragging) = %{version}

%description -n %{name}+uitextdragging
This metapackage enables feature "UITextDragging" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextdropping
Summary:        Bindings to the UIKit framework - feature "UITextDropping"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uitextdropping) = %{version}

%description -n %{name}+uitextdropping
This metapackage enables feature "UITextDropping" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextfield
Summary:        Bindings to the UIKit framework - feature "UITextField"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitextfield) = %{version}

%description -n %{name}+uitextfield
This metapackage enables feature "UITextField" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextformattingcoordinator
Summary:        Bindings to the UIKit framework - feature "UITextFormattingCoordinator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextformattingcoordinator) = %{version}

%description -n %{name}+uitextformattingcoordinator
This metapackage enables feature "UITextFormattingCoordinator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextformattingviewcontrollerchangevalue
Summary:        Bindings to the UIKit framework - feature "UITextFormattingViewControllerChangeValue"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerchangevalue) = %{version}

%description -n %{name}+uitextformattingviewcontrollerchangevalue
This metapackage enables feature "UITextFormattingViewControllerChangeValue" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextformattingviewcontrollerformattingdescriptor
Summary:        Bindings to the UIKit framework - feature "UITextFormattingViewControllerFormattingDescriptor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerformattingdescriptor) = %{version}

%description -n %{name}+uitextformattingviewcontrollerformattingdescriptor
This metapackage enables feature "UITextFormattingViewControllerFormattingDescriptor" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextinput
Summary:        Bindings to the UIKit framework - feature "UITextInput"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextinput) = %{version}

%description -n %{name}+uitextinput
This metapackage enables feature "UITextInput" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextinputtraits
Summary:        Bindings to the UIKit framework - feature "UITextInputTraits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextinputtraits) = %{version}

%description -n %{name}+uitextinputtraits
This metapackage enables feature "UITextInputTraits" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextitem
Summary:        Bindings to the UIKit framework - feature "UITextItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uitextitem) = %{version}

%description -n %{name}+uitextitem
This metapackage enables feature "UITextItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextpastedelegate
Summary:        Bindings to the UIKit framework - feature "UITextPasteDelegate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextpastedelegate) = %{version}

%description -n %{name}+uitextpastedelegate
This metapackage enables feature "UITextPasteDelegate" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextsearching
Summary:        Bindings to the UIKit framework - feature "UITextSearching"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsorderedset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextsearching) = %{version}

%description -n %{name}+uitextsearching
This metapackage enables feature "UITextSearching" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextview
Summary:        Bindings to the UIKit framework - feature "UITextView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitextview) = %{version}

%description -n %{name}+uitextview
This metapackage enables feature "UITextView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitimingparameters
Summary:        Bindings to the UIKit framework - feature "UITimingParameters"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uitimingparameters) = %{version}

%description -n %{name}+uitimingparameters
This metapackage enables feature "UITimingParameters" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitouch
Summary:        Bindings to the UIKit framework - feature "UITouch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitouch) = %{version}

%description -n %{name}+uitouch
This metapackage enables feature "UITouch" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiuseractivity
Summary:        Bindings to the UIKit framework - feature "UIUserActivity" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiuseractivity) = %{version}
Provides:       crate(%{pkgname}/uiwindowsceneactivationconfiguration) = %{version}

%description -n %{name}+uiuseractivity
This metapackage enables feature "UIUserActivity" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIWindowSceneActivationConfiguration" feature.

%package     -n %{name}+uivideoeditorcontroller
Summary:        Bindings to the UIKit framework - feature "UIVideoEditorController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uivideoeditorcontroller) = %{version}

%description -n %{name}+uivideoeditorcontroller
This metapackage enables feature "UIVideoEditorController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiview
Summary:        Bindings to the UIKit framework - feature "UIView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiview) = %{version}

%description -n %{name}+uiview
This metapackage enables feature "UIView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiviewanimating
Summary:        Bindings to the UIKit framework - feature "UIViewAnimating" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewanimating) = %{version}
Provides:       crate(%{pkgname}/uiviewpropertyanimator) = %{version}

%description -n %{name}+uiviewanimating
This metapackage enables feature "UIViewAnimating" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIViewPropertyAnimator" feature.

%package     -n %{name}+uiviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIViewController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsextensioncontext) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsextensionrequesthandling) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewcontroller) = %{version}

%description -n %{name}+uiviewcontroller
This metapackage enables feature "UIViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiviewcontrollertransitioncoordinator
Summary:        Bindings to the UIKit framework - feature "UIViewControllerTransitionCoordinator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewcontrollertransitioncoordinator) = %{version}

%description -n %{name}+uiviewcontrollertransitioncoordinator
This metapackage enables feature "UIViewControllerTransitionCoordinator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiviewcontrollertransitioning
Summary:        Bindings to the UIKit framework - feature "UIViewControllerTransitioning"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewcontrollertransitioning) = %{version}

%description -n %{name}+uiviewcontrollertransitioning
This metapackage enables feature "UIViewControllerTransitioning" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwebview
Summary:        Bindings to the UIKit framework - feature "UIWebView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurlrequest) >= 0.3.2
Provides:       crate(%{pkgname}/uiwebview) = %{version}

%description -n %{name}+uiwebview
This metapackage enables feature "UIWebView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwindow
Summary:        Bindings to the UIKit framework - feature "UIWindow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiwindow) = %{version}

%description -n %{name}+uiwindow
This metapackage enables feature "UIWindow" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwindowscene
Summary:        Bindings to the UIKit framework - feature "UIWindowScene"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/uiscenesizerestrictions) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiwindowscene) = %{version}

%description -n %{name}+uiwindowscene
This metapackage enables feature "UIWindowScene" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwritingtoolscoordinator
Summary:        Bindings to the UIKit framework - feature "UIWritingToolsCoordinator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uiwritingtoolscoordinator) = %{version}

%description -n %{name}+uiwritingtoolscoordinator
This metapackage enables feature "UIWritingToolsCoordinator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwritingtoolscoordinatorcontext
Summary:        Bindings to the UIKit framework - feature "UIWritingToolsCoordinatorContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/uiwritingtoolscoordinatorcontext) = %{version}

%description -n %{name}+uiwritingtoolscoordinatorcontext
This metapackage enables feature "UIWritingToolsCoordinatorContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the UIKit framework - feature "bitflags" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/uidatadetectors) = %{version}
Provides:       crate(%{pkgname}/uiorientation) = %{version}
Provides:       crate(%{pkgname}/uipopoversupport) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIDataDetectors", "UIOrientation", and "UIPopoverSupport" features.

%package     -n %{name}+block2
Summary:        Bindings to the UIKit framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the UIKit framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/documentmanager) = %{version}
Requires:       crate(%{pkgname}/nsadaptiveimageglyph) = %{version}
Requires:       crate(%{pkgname}/nsattributedstring) = %{version}
Requires:       crate(%{pkgname}/nsdataasset) = %{version}
Requires:       crate(%{pkgname}/nsdiffabledatasourcesectionsnapshot) = %{version}
Requires:       crate(%{pkgname}/nsfileproviderextension) = %{version}
Requires:       crate(%{pkgname}/nsindexpath-uikitadditions) = %{version}
Requires:       crate(%{pkgname}/nsitemprovider-uikitadditions) = %{version}
Requires:       crate(%{pkgname}/nslayoutanchor) = %{version}
Requires:       crate(%{pkgname}/nslayoutconstraint) = %{version}
Requires:       crate(%{pkgname}/nslayoutmanager) = %{version}
Requires:       crate(%{pkgname}/nsparagraphstyle) = %{version}
Requires:       crate(%{pkgname}/nsshadow) = %{version}
Requires:       crate(%{pkgname}/nsstringdrawing) = %{version}
Requires:       crate(%{pkgname}/nstext) = %{version}
Requires:       crate(%{pkgname}/nstextattachment) = %{version}
Requires:       crate(%{pkgname}/nstextcontainer) = %{version}
Requires:       crate(%{pkgname}/nstextcontentmanager) = %{version}
Requires:       crate(%{pkgname}/nstextelement) = %{version}
Requires:       crate(%{pkgname}/nstextlayoutfragment) = %{version}
Requires:       crate(%{pkgname}/nstextlayoutmanager) = %{version}
Requires:       crate(%{pkgname}/nstextlinefragment) = %{version}
Requires:       crate(%{pkgname}/nstextlist) = %{version}
Requires:       crate(%{pkgname}/nstextlistelement) = %{version}
Requires:       crate(%{pkgname}/nstextrange) = %{version}
Requires:       crate(%{pkgname}/nstextselection) = %{version}
Requires:       crate(%{pkgname}/nstextselectionnavigation) = %{version}
Requires:       crate(%{pkgname}/nstextstorage) = %{version}
Requires:       crate(%{pkgname}/nstextviewportlayoutcontroller) = %{version}
Requires:       crate(%{pkgname}/nstoolbar-uikitadditions) = %{version}
Requires:       crate(%{pkgname}/nstouchbar-uikitadditions) = %{version}
Requires:       crate(%{pkgname}/nsuseractivity-nsitemprovider) = %{version}
Requires:       crate(%{pkgname}/objc2-cloud-kit) = %{version}
Requires:       crate(%{pkgname}/objc2-core-data) = %{version}
Requires:       crate(%{pkgname}/objc2-core-foundation) = %{version}
Requires:       crate(%{pkgname}/objc2-core-graphics) = %{version}
Requires:       crate(%{pkgname}/objc2-core-image) = %{version}
Requires:       crate(%{pkgname}/objc2-core-location) = %{version}
Requires:       crate(%{pkgname}/objc2-core-text) = %{version}
Requires:       crate(%{pkgname}/objc2-quartz-core) = %{version}
Requires:       crate(%{pkgname}/objc2-user-notifications) = %{version}
Requires:       crate(%{pkgname}/printkitui) = %{version}
Requires:       crate(%{pkgname}/sharesheet) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/uiaccelerometer) = %{version}
Requires:       crate(%{pkgname}/uiaccessibility) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilityadditions) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilityconstants) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilitycontainer) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilitycontentsizecategoryimageadjusting) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilitycustomaction) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilitycustomrotor) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilityelement) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilityidentification) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilitylocationdescriptor) = %{version}
Requires:       crate(%{pkgname}/uiaccessibilityzoom) = %{version}
Requires:       crate(%{pkgname}/uiaction) = %{version}
Requires:       crate(%{pkgname}/uiactionsheet) = %{version}
Requires:       crate(%{pkgname}/uiactivity) = %{version}
Requires:       crate(%{pkgname}/uiactivitycollaborationmoderestriction) = %{version}
Requires:       crate(%{pkgname}/uiactivityindicatorview) = %{version}
Requires:       crate(%{pkgname}/uiactivityitemprovider) = %{version}
Requires:       crate(%{pkgname}/uiactivityitemsconfiguration) = %{version}
Requires:       crate(%{pkgname}/uiactivityitemsconfigurationreading) = %{version}
Requires:       crate(%{pkgname}/uiactivityitemsconfigurationreading-sharesheet) = %{version}
Requires:       crate(%{pkgname}/uiactivityviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uialert) = %{version}
Requires:       crate(%{pkgname}/uialertcontroller) = %{version}
Requires:       crate(%{pkgname}/uialertview) = %{version}
Requires:       crate(%{pkgname}/uiappearance) = %{version}
Requires:       crate(%{pkgname}/uiapplication) = %{version}
Requires:       crate(%{pkgname}/uiapplicationshortcutitem) = %{version}
Requires:       crate(%{pkgname}/uiattachmentbehavior) = %{version}
Requires:       crate(%{pkgname}/uibackgroundconfiguration) = %{version}
Requires:       crate(%{pkgname}/uibackgroundextensionview) = %{version}
Requires:       crate(%{pkgname}/uibandselectioninteraction) = %{version}
Requires:       crate(%{pkgname}/uibarappearance) = %{version}
Requires:       crate(%{pkgname}/uibarbuttonitem) = %{version}
Requires:       crate(%{pkgname}/uibarbuttonitemappearance) = %{version}
Requires:       crate(%{pkgname}/uibarbuttonitembadge) = %{version}
Requires:       crate(%{pkgname}/uibarbuttonitemgroup) = %{version}
Requires:       crate(%{pkgname}/uibarcommon) = %{version}
Requires:       crate(%{pkgname}/uibaritem) = %{version}
Requires:       crate(%{pkgname}/uibehavioralstyle) = %{version}
Requires:       crate(%{pkgname}/uibezierpath) = %{version}
Requires:       crate(%{pkgname}/uiblureffect) = %{version}
Requires:       crate(%{pkgname}/uibutton) = %{version}
Requires:       crate(%{pkgname}/uibuttonconfiguration) = %{version}
Requires:       crate(%{pkgname}/uicalendarselection) = %{version}
Requires:       crate(%{pkgname}/uicalendarselectionmultidate) = %{version}
Requires:       crate(%{pkgname}/uicalendarselectionsingledate) = %{version}
Requires:       crate(%{pkgname}/uicalendarselectionweekofyear) = %{version}
Requires:       crate(%{pkgname}/uicalendarview) = %{version}
Requires:       crate(%{pkgname}/uicalendarviewdecoration) = %{version}
Requires:       crate(%{pkgname}/uicanvasfeedbackgenerator) = %{version}
Requires:       crate(%{pkgname}/uicellaccessory) = %{version}
Requires:       crate(%{pkgname}/uicellconfigurationstate) = %{version}
Requires:       crate(%{pkgname}/uicloudsharingcontroller) = %{version}
Requires:       crate(%{pkgname}/uicollectionlayoutlist) = %{version}
Requires:       crate(%{pkgname}/uicollectionview) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewcell) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewcompositionallayout) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewflowlayout) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewitemregistration) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewlayout) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewlistcell) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewtransitionlayout) = %{version}
Requires:       crate(%{pkgname}/uicollectionviewupdateitem) = %{version}
Requires:       crate(%{pkgname}/uicollisionbehavior) = %{version}
Requires:       crate(%{pkgname}/uicolor) = %{version}
Requires:       crate(%{pkgname}/uicolorpickerviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uicolorwell) = %{version}
Requires:       crate(%{pkgname}/uicommand) = %{version}
Requires:       crate(%{pkgname}/uiconfigurationcolortransformer) = %{version}
Requires:       crate(%{pkgname}/uiconfigurationstate) = %{version}
Requires:       crate(%{pkgname}/uicontentconfiguration) = %{version}
Requires:       crate(%{pkgname}/uicontentsizecategory) = %{version}
Requires:       crate(%{pkgname}/uicontentsizecategoryadjusting) = %{version}
Requires:       crate(%{pkgname}/uicontentunavailablebuttonproperties) = %{version}
Requires:       crate(%{pkgname}/uicontentunavailableconfiguration) = %{version}
Requires:       crate(%{pkgname}/uicontentunavailableconfigurationstate) = %{version}
Requires:       crate(%{pkgname}/uicontentunavailableimageproperties) = %{version}
Requires:       crate(%{pkgname}/uicontentunavailabletextproperties) = %{version}
Requires:       crate(%{pkgname}/uicontentunavailableview) = %{version}
Requires:       crate(%{pkgname}/uicontextmenuconfiguration) = %{version}
Requires:       crate(%{pkgname}/uicontextmenuinteraction) = %{version}
Requires:       crate(%{pkgname}/uicontextmenusystem) = %{version}
Requires:       crate(%{pkgname}/uicontextualaction) = %{version}
Requires:       crate(%{pkgname}/uicontrol) = %{version}
Requires:       crate(%{pkgname}/uiconversationcontext) = %{version}
Requires:       crate(%{pkgname}/uiconversationentry) = %{version}
Requires:       crate(%{pkgname}/uicornerconfiguration) = %{version}
Requires:       crate(%{pkgname}/uicornerradius) = %{version}
Requires:       crate(%{pkgname}/uidatadetectors) = %{version}
Requires:       crate(%{pkgname}/uidatasourcetranslating) = %{version}
Requires:       crate(%{pkgname}/uidatepicker) = %{version}
Requires:       crate(%{pkgname}/uideferredmenuelement) = %{version}
Requires:       crate(%{pkgname}/uidevice) = %{version}
Requires:       crate(%{pkgname}/uidiffabledatasource) = %{version}
Requires:       crate(%{pkgname}/uidocument) = %{version}
Requires:       crate(%{pkgname}/uidocumentbrowseraction) = %{version}
Requires:       crate(%{pkgname}/uidocumentbrowserviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uidocumentinteractioncontroller) = %{version}
Requires:       crate(%{pkgname}/uidocumentmenuviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uidocumentpickerextensionviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uidocumentpickerviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uidocumentproperties) = %{version}
Requires:       crate(%{pkgname}/uidocumentviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uidocumentviewcontrollerlaunchoptions) = %{version}
Requires:       crate(%{pkgname}/uidraginteraction) = %{version}
Requires:       crate(%{pkgname}/uidragitem) = %{version}
Requires:       crate(%{pkgname}/uidragpreview) = %{version}
Requires:       crate(%{pkgname}/uidragpreviewparameters) = %{version}
Requires:       crate(%{pkgname}/uidragsession) = %{version}
Requires:       crate(%{pkgname}/uidropinteraction) = %{version}
Requires:       crate(%{pkgname}/uidynamicanimator) = %{version}
Requires:       crate(%{pkgname}/uidynamicbehavior) = %{version}
Requires:       crate(%{pkgname}/uidynamicitembehavior) = %{version}
Requires:       crate(%{pkgname}/uieditmenuinteraction) = %{version}
Requires:       crate(%{pkgname}/uievent) = %{version}
Requires:       crate(%{pkgname}/uieventattribution) = %{version}
Requires:       crate(%{pkgname}/uieventattributionview) = %{version}
Requires:       crate(%{pkgname}/uifeedbackgenerator) = %{version}
Requires:       crate(%{pkgname}/uifieldbehavior) = %{version}
Requires:       crate(%{pkgname}/uifindinteraction) = %{version}
Requires:       crate(%{pkgname}/uifindsession) = %{version}
Requires:       crate(%{pkgname}/uifocus) = %{version}
Requires:       crate(%{pkgname}/uifocusanimationcoordinator) = %{version}
Requires:       crate(%{pkgname}/uifocusdebugger) = %{version}
Requires:       crate(%{pkgname}/uifocusdefines) = %{version}
Requires:       crate(%{pkgname}/uifocuseffect) = %{version}
Requires:       crate(%{pkgname}/uifocusguide) = %{version}
Requires:       crate(%{pkgname}/uifocusmovementhint) = %{version}
Requires:       crate(%{pkgname}/uifocussystem) = %{version}
Requires:       crate(%{pkgname}/uifocussystem-uikitadditions) = %{version}
Requires:       crate(%{pkgname}/uifocusupdatecontext-uikitadditions) = %{version}
Requires:       crate(%{pkgname}/uifont) = %{version}
Requires:       crate(%{pkgname}/uifontdescriptor) = %{version}
Requires:       crate(%{pkgname}/uifontmetrics) = %{version}
Requires:       crate(%{pkgname}/uifontpickerviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uifontpickerviewcontrollerconfiguration) = %{version}
Requires:       crate(%{pkgname}/uifoundation) = %{version}
Requires:       crate(%{pkgname}/uigeometry) = %{version}
Requires:       crate(%{pkgname}/uigesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uigesturerecognizersubclass) = %{version}
Requires:       crate(%{pkgname}/uiglasseffect) = %{version}
Requires:       crate(%{pkgname}/uigraphics) = %{version}
Requires:       crate(%{pkgname}/uigraphicsimagerenderer) = %{version}
Requires:       crate(%{pkgname}/uigraphicspdfrenderer) = %{version}
Requires:       crate(%{pkgname}/uigraphicsrenderer) = %{version}
Requires:       crate(%{pkgname}/uigraphicsrenderersubclass) = %{version}
Requires:       crate(%{pkgname}/uigravitybehavior) = %{version}
Requires:       crate(%{pkgname}/uiguidedaccess) = %{version}
Requires:       crate(%{pkgname}/uiguidedaccessrestrictions) = %{version}
Requires:       crate(%{pkgname}/uihovereffect) = %{version}
Requires:       crate(%{pkgname}/uihovereffectlayer) = %{version}
Requires:       crate(%{pkgname}/uihovergesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uihoverstyle) = %{version}
Requires:       crate(%{pkgname}/uiimage) = %{version}
Requires:       crate(%{pkgname}/uiimageasset) = %{version}
Requires:       crate(%{pkgname}/uiimageconfiguration) = %{version}
Requires:       crate(%{pkgname}/uiimagepickercontroller) = %{version}
Requires:       crate(%{pkgname}/uiimagereader) = %{version}
Requires:       crate(%{pkgname}/uiimagesymbolconfiguration) = %{version}
Requires:       crate(%{pkgname}/uiimageview) = %{version}
Requires:       crate(%{pkgname}/uiimpactfeedbackgenerator) = %{version}
Requires:       crate(%{pkgname}/uiindirectscribbleinteraction) = %{version}
Requires:       crate(%{pkgname}/uiinputsuggestion) = %{version}
Requires:       crate(%{pkgname}/uiinputview) = %{version}
Requires:       crate(%{pkgname}/uiinputviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uiinteraction) = %{version}
Requires:       crate(%{pkgname}/uiinterface) = %{version}
Requires:       crate(%{pkgname}/uikey) = %{version}
Requires:       crate(%{pkgname}/uikeyboardlayoutguide) = %{version}
Requires:       crate(%{pkgname}/uikeycommand) = %{version}
Requires:       crate(%{pkgname}/uikeyconstants) = %{version}
Requires:       crate(%{pkgname}/uikitcore) = %{version}
Requires:       crate(%{pkgname}/uikitdefines) = %{version}
Requires:       crate(%{pkgname}/uilabel) = %{version}
Requires:       crate(%{pkgname}/uilargecontentviewer) = %{version}
Requires:       crate(%{pkgname}/uilayoutguide) = %{version}
Requires:       crate(%{pkgname}/uiletterformawareadjusting) = %{version}
Requires:       crate(%{pkgname}/uilexicon) = %{version}
Requires:       crate(%{pkgname}/uilistcontentconfiguration) = %{version}
Requires:       crate(%{pkgname}/uilistcontentimageproperties) = %{version}
Requires:       crate(%{pkgname}/uilistcontenttextproperties) = %{version}
Requires:       crate(%{pkgname}/uilistseparatorconfiguration) = %{version}
Requires:       crate(%{pkgname}/uilocalizedindexedcollation) = %{version}
Requires:       crate(%{pkgname}/uilocalnotification) = %{version}
Requires:       crate(%{pkgname}/uilongpressgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uimailconversationcontext) = %{version}
Requires:       crate(%{pkgname}/uimailconversationentry) = %{version}
Requires:       crate(%{pkgname}/uimainmenusystem) = %{version}
Requires:       crate(%{pkgname}/uimanageddocument) = %{version}
Requires:       crate(%{pkgname}/uimenu) = %{version}
Requires:       crate(%{pkgname}/uimenubuilder) = %{version}
Requires:       crate(%{pkgname}/uimenucontroller) = %{version}
Requires:       crate(%{pkgname}/uimenudisplaypreferences) = %{version}
Requires:       crate(%{pkgname}/uimenuelement) = %{version}
Requires:       crate(%{pkgname}/uimenuleaf) = %{version}
Requires:       crate(%{pkgname}/uimenusystem) = %{version}
Requires:       crate(%{pkgname}/uimessageconversationcontext) = %{version}
Requires:       crate(%{pkgname}/uimessageconversationentry) = %{version}
Requires:       crate(%{pkgname}/uimotioneffect) = %{version}
Requires:       crate(%{pkgname}/uinavigationbar) = %{version}
Requires:       crate(%{pkgname}/uinavigationbarappearance) = %{version}
Requires:       crate(%{pkgname}/uinavigationcontroller) = %{version}
Requires:       crate(%{pkgname}/uinavigationitem) = %{version}
Requires:       crate(%{pkgname}/uinib) = %{version}
Requires:       crate(%{pkgname}/uinibdeclarations) = %{version}
Requires:       crate(%{pkgname}/uinibloading) = %{version}
Requires:       crate(%{pkgname}/uinotificationfeedbackgenerator) = %{version}
Requires:       crate(%{pkgname}/uiopenurlcontext) = %{version}
Requires:       crate(%{pkgname}/uiorientation) = %{version}
Requires:       crate(%{pkgname}/uipagecontrol) = %{version}
Requires:       crate(%{pkgname}/uipagecontrolprogress) = %{version}
Requires:       crate(%{pkgname}/uipageviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uipangesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uipasteboard) = %{version}
Requires:       crate(%{pkgname}/uipasteconfiguration) = %{version}
Requires:       crate(%{pkgname}/uipasteconfigurationsupporting) = %{version}
Requires:       crate(%{pkgname}/uipastecontrol) = %{version}
Requires:       crate(%{pkgname}/uipencilinteraction) = %{version}
Requires:       crate(%{pkgname}/uipickerview) = %{version}
Requires:       crate(%{pkgname}/uipinchgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uipointeraccessory) = %{version}
Requires:       crate(%{pkgname}/uipointerinteraction) = %{version}
Requires:       crate(%{pkgname}/uipointerlockstate) = %{version}
Requires:       crate(%{pkgname}/uipointerregion) = %{version}
Requires:       crate(%{pkgname}/uipointerstyle) = %{version}
Requires:       crate(%{pkgname}/uipopoverbackgroundview) = %{version}
Requires:       crate(%{pkgname}/uipopovercontroller) = %{version}
Requires:       crate(%{pkgname}/uipopoverpresentationcontroller) = %{version}
Requires:       crate(%{pkgname}/uipopoverpresentationcontrollersourceitem) = %{version}
Requires:       crate(%{pkgname}/uipopoversupport) = %{version}
Requires:       crate(%{pkgname}/uipresentationcontroller) = %{version}
Requires:       crate(%{pkgname}/uipress) = %{version}
Requires:       crate(%{pkgname}/uipressesevent) = %{version}
Requires:       crate(%{pkgname}/uipreviewinteraction) = %{version}
Requires:       crate(%{pkgname}/uipreviewparameters) = %{version}
Requires:       crate(%{pkgname}/uiprinter) = %{version}
Requires:       crate(%{pkgname}/uiprinterpickercontroller) = %{version}
Requires:       crate(%{pkgname}/uiprinterror) = %{version}
Requires:       crate(%{pkgname}/uiprintformatter) = %{version}
Requires:       crate(%{pkgname}/uiprintinfo) = %{version}
Requires:       crate(%{pkgname}/uiprintinteractioncontroller) = %{version}
Requires:       crate(%{pkgname}/uiprintpagerenderer) = %{version}
Requires:       crate(%{pkgname}/uiprintpaper) = %{version}
Requires:       crate(%{pkgname}/uiprintserviceextension) = %{version}
Requires:       crate(%{pkgname}/uiprogressview) = %{version}
Requires:       crate(%{pkgname}/uipushbehavior) = %{version}
Requires:       crate(%{pkgname}/uireferencelibraryviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uirefreshcontrol) = %{version}
Requires:       crate(%{pkgname}/uiregion) = %{version}
Requires:       crate(%{pkgname}/uiresponder) = %{version}
Requires:       crate(%{pkgname}/uiresponder-uiactivityitemsconfiguration) = %{version}
Requires:       crate(%{pkgname}/uirotationgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uiscene) = %{version}
Requires:       crate(%{pkgname}/uiscene-avaudiosession) = %{version}
Requires:       crate(%{pkgname}/uisceneactivationconditions) = %{version}
Requires:       crate(%{pkgname}/uisceneconfiguration) = %{version}
Requires:       crate(%{pkgname}/uiscenedefinitions) = %{version}
Requires:       crate(%{pkgname}/uiscenedestructioncondition) = %{version}
Requires:       crate(%{pkgname}/uisceneenhancedstaterestoration) = %{version}
Requires:       crate(%{pkgname}/uisceneoptions) = %{version}
Requires:       crate(%{pkgname}/uiscenesession) = %{version}
Requires:       crate(%{pkgname}/uiscenesessionactivationrequest) = %{version}
Requires:       crate(%{pkgname}/uiscenesizerestrictions) = %{version}
Requires:       crate(%{pkgname}/uiscenesystemprotectionmanager) = %{version}
Requires:       crate(%{pkgname}/uiscenewindowingbehaviors) = %{version}
Requires:       crate(%{pkgname}/uiscenewindowingcontrolstyle) = %{version}
Requires:       crate(%{pkgname}/uiscreen) = %{version}
Requires:       crate(%{pkgname}/uiscreenedgepangesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uiscreenmode) = %{version}
Requires:       crate(%{pkgname}/uiscreenshotservice) = %{version}
Requires:       crate(%{pkgname}/uiscribbleinteraction) = %{version}
Requires:       crate(%{pkgname}/uiscrolledgeelementcontainerinteraction) = %{version}
Requires:       crate(%{pkgname}/uiscrollview) = %{version}
Requires:       crate(%{pkgname}/uisearchbar) = %{version}
Requires:       crate(%{pkgname}/uisearchcontainerviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uisearchcontroller) = %{version}
Requires:       crate(%{pkgname}/uisearchdisplaycontroller) = %{version}
Requires:       crate(%{pkgname}/uisearchsuggestion) = %{version}
Requires:       crate(%{pkgname}/uisearchtab) = %{version}
Requires:       crate(%{pkgname}/uisearchtextfield) = %{version}
Requires:       crate(%{pkgname}/uisegmentedcontrol) = %{version}
Requires:       crate(%{pkgname}/uiselectionfeedbackgenerator) = %{version}
Requires:       crate(%{pkgname}/uishadowproperties) = %{version}
Requires:       crate(%{pkgname}/uishape) = %{version}
Requires:       crate(%{pkgname}/uisheetpresentationcontroller) = %{version}
Requires:       crate(%{pkgname}/uislider) = %{version}
Requires:       crate(%{pkgname}/uislidertrackconfiguration) = %{version}
Requires:       crate(%{pkgname}/uismartreplysuggestion) = %{version}
Requires:       crate(%{pkgname}/uisnapbehavior) = %{version}
Requires:       crate(%{pkgname}/uisplitviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uisplitviewcontrollerlayoutenvironment) = %{version}
Requires:       crate(%{pkgname}/uispringloadedinteraction) = %{version}
Requires:       crate(%{pkgname}/uispringloadedinteractionsupporting) = %{version}
Requires:       crate(%{pkgname}/uistackview) = %{version}
Requires:       crate(%{pkgname}/uistandardtextcursorview) = %{version}
Requires:       crate(%{pkgname}/uistaterestoration) = %{version}
Requires:       crate(%{pkgname}/uistatusbarmanager) = %{version}
Requires:       crate(%{pkgname}/uistepper) = %{version}
Requires:       crate(%{pkgname}/uistoryboard) = %{version}
Requires:       crate(%{pkgname}/uistoryboardpopoversegue) = %{version}
Requires:       crate(%{pkgname}/uistoryboardsegue) = %{version}
Requires:       crate(%{pkgname}/uistringdrawing) = %{version}
Requires:       crate(%{pkgname}/uiswipeactionsconfiguration) = %{version}
Requires:       crate(%{pkgname}/uiswipegesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uiswitch) = %{version}
Requires:       crate(%{pkgname}/uisymbolcontenttransition) = %{version}
Requires:       crate(%{pkgname}/uisymboleffectcompletion) = %{version}
Requires:       crate(%{pkgname}/uitab) = %{version}
Requires:       crate(%{pkgname}/uitabaccessory) = %{version}
Requires:       crate(%{pkgname}/uitabbar) = %{version}
Requires:       crate(%{pkgname}/uitabbarappearance) = %{version}
Requires:       crate(%{pkgname}/uitabbarcontroller) = %{version}
Requires:       crate(%{pkgname}/uitabbarcontrollersidebar) = %{version}
Requires:       crate(%{pkgname}/uitabbaritem) = %{version}
Requires:       crate(%{pkgname}/uitabgroup) = %{version}
Requires:       crate(%{pkgname}/uitableview) = %{version}
Requires:       crate(%{pkgname}/uitableviewcell) = %{version}
Requires:       crate(%{pkgname}/uitableviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uitableviewheaderfooterview) = %{version}
Requires:       crate(%{pkgname}/uitabsidebaritem) = %{version}
Requires:       crate(%{pkgname}/uitapgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/uitargeteddragpreview) = %{version}
Requires:       crate(%{pkgname}/uitargetedpreview) = %{version}
Requires:       crate(%{pkgname}/uitextchecker) = %{version}
Requires:       crate(%{pkgname}/uitextcursordroppositionanimator) = %{version}
Requires:       crate(%{pkgname}/uitextcursorview) = %{version}
Requires:       crate(%{pkgname}/uitextdragging) = %{version}
Requires:       crate(%{pkgname}/uitextdragpreviewrenderer) = %{version}
Requires:       crate(%{pkgname}/uitextdragurlpreviews) = %{version}
Requires:       crate(%{pkgname}/uitextdropping) = %{version}
Requires:       crate(%{pkgname}/uitextdropproposal) = %{version}
Requires:       crate(%{pkgname}/uitextfield) = %{version}
Requires:       crate(%{pkgname}/uitextformattingcoordinator) = %{version}
Requires:       crate(%{pkgname}/uitextformattingviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerchangevalue) = %{version}
Requires:       crate(%{pkgname}/uitextformattingviewcontrollercomponent) = %{version}
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerconfiguration) = %{version}
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerformattingdescriptor) = %{version}
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerformattingstyle) = %{version}
Requires:       crate(%{pkgname}/uitextinput) = %{version}
Requires:       crate(%{pkgname}/uitextinputcontext) = %{version}
Requires:       crate(%{pkgname}/uitextinputtraits) = %{version}
Requires:       crate(%{pkgname}/uitextinteraction) = %{version}
Requires:       crate(%{pkgname}/uitextitem) = %{version}
Requires:       crate(%{pkgname}/uitextiteminteraction) = %{version}
Requires:       crate(%{pkgname}/uitextloupesession) = %{version}
Requires:       crate(%{pkgname}/uitextpasteconfigurationsupporting) = %{version}
Requires:       crate(%{pkgname}/uitextpastedelegate) = %{version}
Requires:       crate(%{pkgname}/uitextsearching) = %{version}
Requires:       crate(%{pkgname}/uitextselectiondisplayinteraction) = %{version}
Requires:       crate(%{pkgname}/uitextselectionhandleview) = %{version}
Requires:       crate(%{pkgname}/uitextselectionhighlightview) = %{version}
Requires:       crate(%{pkgname}/uitextview) = %{version}
Requires:       crate(%{pkgname}/uitimingcurveprovider) = %{version}
Requires:       crate(%{pkgname}/uitimingparameters) = %{version}
Requires:       crate(%{pkgname}/uitoolbar) = %{version}
Requires:       crate(%{pkgname}/uitoolbarappearance) = %{version}
Requires:       crate(%{pkgname}/uitooltipinteraction) = %{version}
Requires:       crate(%{pkgname}/uitouch) = %{version}
Requires:       crate(%{pkgname}/uitrackinglayoutguide) = %{version}
Requires:       crate(%{pkgname}/uitrait) = %{version}
Requires:       crate(%{pkgname}/uitraitcollection) = %{version}
Requires:       crate(%{pkgname}/uitraitlistenvironment) = %{version}
Requires:       crate(%{pkgname}/uiupdateactionphase) = %{version}
Requires:       crate(%{pkgname}/uiupdateinfo) = %{version}
Requires:       crate(%{pkgname}/uiupdatelink) = %{version}
Requires:       crate(%{pkgname}/uiuseractivity) = %{version}
Requires:       crate(%{pkgname}/uiusernotificationsettings) = %{version}
Requires:       crate(%{pkgname}/uivibrancyeffect) = %{version}
Requires:       crate(%{pkgname}/uivideoeditorcontroller) = %{version}
Requires:       crate(%{pkgname}/uiview) = %{version}
Requires:       crate(%{pkgname}/uiviewanimating) = %{version}
Requires:       crate(%{pkgname}/uiviewconfigurationstate) = %{version}
Requires:       crate(%{pkgname}/uiviewcontroller) = %{version}
Requires:       crate(%{pkgname}/uiviewcontrollertransition) = %{version}
Requires:       crate(%{pkgname}/uiviewcontrollertransitioncoordinator) = %{version}
Requires:       crate(%{pkgname}/uiviewcontrollertransitioning) = %{version}
Requires:       crate(%{pkgname}/uiviewlayoutregion) = %{version}
Requires:       crate(%{pkgname}/uiviewpropertyanimator) = %{version}
Requires:       crate(%{pkgname}/uivisualeffect) = %{version}
Requires:       crate(%{pkgname}/uivisualeffectview) = %{version}
Requires:       crate(%{pkgname}/uiwebview) = %{version}
Requires:       crate(%{pkgname}/uiwindow) = %{version}
Requires:       crate(%{pkgname}/uiwindowscene) = %{version}
Requires:       crate(%{pkgname}/uiwindowsceneactivationaction) = %{version}
Requires:       crate(%{pkgname}/uiwindowsceneactivationconfiguration) = %{version}
Requires:       crate(%{pkgname}/uiwindowsceneactivationinteraction) = %{version}
Requires:       crate(%{pkgname}/uiwindowsceneactivationrequestoptions) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenedraginteraction) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenegeometry) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferences) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferencesios) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferencesmac) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferencesvision) = %{version}
Requires:       crate(%{pkgname}/uiwindowsceneplacement) = %{version}
Requires:       crate(%{pkgname}/uiwindowsceneprominentplacement) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenepushplacement) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenereplaceplacement) = %{version}
Requires:       crate(%{pkgname}/uiwindowscenestandardplacement) = %{version}
Requires:       crate(%{pkgname}/uiwritingtoolscoordinator) = %{version}
Requires:       crate(%{pkgname}/uiwritingtoolscoordinatoranimationparameters) = %{version}
Requires:       crate(%{pkgname}/uiwritingtoolscoordinatorcontext) = %{version}
Requires:       crate(%{pkgname}/uizoomtransitionoptions) = %{version}
Requires:       crate(%{pkgname}/unnotificationresponse-uikitadditions) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-cloud-kit
Summary:        Bindings to the UIKit framework - feature "objc2-cloud-kit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-cloud-kit-0.3/ckcontainer) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckrecord) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckshare) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/cksharemetadata) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-cloud-kit) = %{version}

%description -n %{name}+objc2-cloud-kit
This metapackage enables feature "objc2-cloud-kit" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-data
Summary:        Bindings to the UIKit framework - feature "objc2-core-data"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-data-0.3/nsmanagedobjectcontext) >= 0.3.2
Requires:       crate(objc2-core-data-0.3/nsmanagedobjectmodel) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-data) = %{version}

%description -n %{name}+objc2-core-data
This metapackage enables feature "objc2-core-data" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Bindings to the UIKit framework - feature "objc2-core-foundation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-foundation) = %{version}

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-graphics
Summary:        Bindings to the UIKit framework - feature "objc2-core-graphics"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-graphics-0.3/cgcolor) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgfont) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgimage) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgpath) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-graphics) = %{version}

%description -n %{name}+objc2-core-graphics
This metapackage enables feature "objc2-core-graphics" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-image
Summary:        Bindings to the UIKit framework - feature "objc2-core-image"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-image-0.3/cicolor) >= 0.3.2
Requires:       crate(objc2-core-image-0.3/ciimage) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-image) = %{version}

%description -n %{name}+objc2-core-image
This metapackage enables feature "objc2-core-image" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-location
Summary:        Bindings to the UIKit framework - feature "objc2-core-location"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.3/clregion) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-location) = %{version}

%description -n %{name}+objc2-core-location
This metapackage enables feature "objc2-core-location" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-text
Summary:        Bindings to the UIKit framework - feature "objc2-core-text"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-text-0.3/ctfont) >= 0.3.2
Requires:       crate(objc2-core-text-0.3/ctfontdescriptor) >= 0.3.2
Requires:       crate(objc2-core-text-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-text) = %{version}

%description -n %{name}+objc2-core-text
This metapackage enables feature "objc2-core-text" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-quartz-core
Summary:        Bindings to the UIKit framework - feature "objc2-quartz-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-quartz-core-0.3/cadisplaylink) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/caframeraterange) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/calayer) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/camediatiming) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/catransform3d) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/objc2-core-foundation) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-quartz-core) = %{version}

%description -n %{name}+objc2-quartz-core
This metapackage enables feature "objc2-quartz-core" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-symbols
Summary:        Bindings to the UIKit framework - feature "objc2-symbols"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-symbols-0.3/nssymboleffect) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-symbols) = %{version}

%description -n %{name}+objc2-symbols
This metapackage enables feature "objc2-symbols" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-uniform-type-identifiers
Summary:        Bindings to the UIKit framework - feature "objc2-uniform-type-identifiers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-uniform-type-identifiers-0.3/uttype) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-uniform-type-identifiers) = %{version}

%description -n %{name}+objc2-uniform-type-identifiers
This metapackage enables feature "objc2-uniform-type-identifiers" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-user-notifications
Summary:        Bindings to the UIKit framework - feature "objc2-user-notifications"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-user-notifications-0.3/unnotificationresponse) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-user-notifications) = %{version}

%description -n %{name}+objc2-user-notifications
This metapackage enables feature "objc2-user-notifications" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
