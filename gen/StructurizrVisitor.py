# Generated from C:/Users/pmora/Documents/Git/GitHub/DesignShift/Structurizr.g4 by ANTLR 4.13.1
import antlr4
if "." in __name__:
    from .StructurizrParser import StructurizrParser
else:
    from StructurizrParser import StructurizrParser

# This class defines a complete generic visitor for a parse tree produced by StructurizrParser.

class StructurizrVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StructurizrParser#workspace.
    def visitWorkspace(self, ctx:StructurizrParser.WorkspaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#workspace_body.
    def visitWorkspace_body(self, ctx:StructurizrParser.Workspace_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#model.
    def visitModel(self, ctx:StructurizrParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#model_body.
    def visitModel_body(self, ctx:StructurizrParser.Model_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#person.
    def visitPerson(self, ctx:StructurizrParser.PersonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#person_body.
    def visitPerson_body(self, ctx:StructurizrParser.Person_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#softwareSystem.
    def visitSoftwareSystem(self, ctx:StructurizrParser.SoftwareSystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#softwareSystem_body.
    def visitSoftwareSystem_body(self, ctx:StructurizrParser.SoftwareSystem_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#container.
    def visitContainer(self, ctx:StructurizrParser.ContainerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#container_body.
    def visitContainer_body(self, ctx:StructurizrParser.Container_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#component.
    def visitComponent(self, ctx:StructurizrParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#component_body.
    def visitComponent_body(self, ctx:StructurizrParser.Component_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#deploymentNode.
    def visitDeploymentNode(self, ctx:StructurizrParser.DeploymentNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#deploymentNode_body.
    def visitDeploymentNode_body(self, ctx:StructurizrParser.DeploymentNode_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#infrastructureNode.
    def visitInfrastructureNode(self, ctx:StructurizrParser.InfrastructureNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#infrastructureNode_body.
    def visitInfrastructureNode_body(self, ctx:StructurizrParser.InfrastructureNode_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#softwareSystemInstance.
    def visitSoftwareSystemInstance(self, ctx:StructurizrParser.SoftwareSystemInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#softwareSystemInstance_body.
    def visitSoftwareSystemInstance_body(self, ctx:StructurizrParser.SoftwareSystemInstance_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#deploymentGroups.
    def visitDeploymentGroups(self, ctx:StructurizrParser.DeploymentGroupsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#deploymentGroup.
    def visitDeploymentGroup(self, ctx:StructurizrParser.DeploymentGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#containerInstance.
    def visitContainerInstance(self, ctx:StructurizrParser.ContainerInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#container_inst_body.
    def visitContainer_inst_body(self, ctx:StructurizrParser.Container_inst_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#healthCheck.
    def visitHealthCheck(self, ctx:StructurizrParser.HealthCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#interval.
    def visitInterval(self, ctx:StructurizrParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#timeout.
    def visitTimeout(self, ctx:StructurizrParser.TimeoutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#relationship.
    def visitRelationship(self, ctx:StructurizrParser.RelationshipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#relationship_body.
    def visitRelationship_body(self, ctx:StructurizrParser.Relationship_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#perspectives.
    def visitPerspectives(self, ctx:StructurizrParser.PerspectivesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#perspectives_body.
    def visitPerspectives_body(self, ctx:StructurizrParser.Perspectives_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#views.
    def visitViews(self, ctx:StructurizrParser.ViewsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#views_body.
    def visitViews_body(self, ctx:StructurizrParser.Views_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#systemLandscapeView.
    def visitSystemLandscapeView(self, ctx:StructurizrParser.SystemLandscapeViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#view_body.
    def visitView_body(self, ctx:StructurizrParser.View_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#paperSize.
    def visitPaperSize(self, ctx:StructurizrParser.PaperSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#systemContextView.
    def visitSystemContextView(self, ctx:StructurizrParser.SystemContextViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#automaticLayout.
    def visitAutomaticLayout(self, ctx:StructurizrParser.AutomaticLayoutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#rankSeparation.
    def visitRankSeparation(self, ctx:StructurizrParser.RankSeparationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#nodeSeparation.
    def visitNodeSeparation(self, ctx:StructurizrParser.NodeSeparationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#default.
    def visitDefault(self, ctx:StructurizrParser.DefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#include.
    def visitInclude(self, ctx:StructurizrParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#exclude.
    def visitExclude(self, ctx:StructurizrParser.ExcludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#containerView.
    def visitContainerView(self, ctx:StructurizrParser.ContainerViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#componentView.
    def visitComponentView(self, ctx:StructurizrParser.ComponentViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#filteredView.
    def visitFilteredView(self, ctx:StructurizrParser.FilteredViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#filtered_body.
    def visitFiltered_body(self, ctx:StructurizrParser.Filtered_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#dynamicView.
    def visitDynamicView(self, ctx:StructurizrParser.DynamicViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#dynamicView_body.
    def visitDynamicView_body(self, ctx:StructurizrParser.DynamicView_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#deploymentEnvironment.
    def visitDeploymentEnvironment(self, ctx:StructurizrParser.DeploymentEnvironmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#dep_env_body.
    def visitDep_env_body(self, ctx:StructurizrParser.Dep_env_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#deploymentView.
    def visitDeploymentView(self, ctx:StructurizrParser.DeploymentViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#deployment_view_body.
    def visitDeployment_view_body(self, ctx:StructurizrParser.Deployment_view_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#environment.
    def visitEnvironment(self, ctx:StructurizrParser.EnvironmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#imageView.
    def visitImageView(self, ctx:StructurizrParser.ImageViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#imageView_body.
    def visitImageView_body(self, ctx:StructurizrParser.ImageView_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#customElement.
    def visitCustomElement(self, ctx:StructurizrParser.CustomElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#custom_element_body.
    def visitCustom_element_body(self, ctx:StructurizrParser.Custom_element_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#elementView.
    def visitElementView(self, ctx:StructurizrParser.ElementViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#elementView_body.
    def visitElementView_body(self, ctx:StructurizrParser.ElementView_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#metadata.
    def visitMetadata(self, ctx:StructurizrParser.MetadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#relationshipView.
    def visitRelationshipView(self, ctx:StructurizrParser.RelationshipViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#relationshipView_body.
    def visitRelationshipView_body(self, ctx:StructurizrParser.RelationshipView_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#pair.
    def visitPair(self, ctx:StructurizrParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#array.
    def visitArray(self, ctx:StructurizrParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#animation.
    def visitAnimation(self, ctx:StructurizrParser.AnimationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#animation_body.
    def visitAnimation_body(self, ctx:StructurizrParser.Animation_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#dimensions.
    def visitDimensions(self, ctx:StructurizrParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#configuration.
    def visitConfiguration(self, ctx:StructurizrParser.ConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#configuration_body.
    def visitConfiguration_body(self, ctx:StructurizrParser.Configuration_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#styles.
    def visitStyles(self, ctx:StructurizrParser.StylesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#style_body.
    def visitStyle_body(self, ctx:StructurizrParser.Style_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#customView.
    def visitCustomView(self, ctx:StructurizrParser.CustomViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#custom_body.
    def visitCustom_body(self, ctx:StructurizrParser.Custom_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#elementStyle.
    def visitElementStyle(self, ctx:StructurizrParser.ElementStyleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#element_style_body.
    def visitElement_style_body(self, ctx:StructurizrParser.Element_style_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#shapetype.
    def visitShapetype(self, ctx:StructurizrParser.ShapetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#relationshipStyle.
    def visitRelationshipStyle(self, ctx:StructurizrParser.RelationshipStyleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#rel_style_body.
    def visitRel_style_body(self, ctx:StructurizrParser.Rel_style_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#routingType.
    def visitRoutingType(self, ctx:StructurizrParser.RoutingTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#styleType.
    def visitStyleType(self, ctx:StructurizrParser.StyleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_docs.
    def visitBang_docs(self, ctx:StructurizrParser.Bang_docsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_adrs.
    def visitBang_adrs(self, ctx:StructurizrParser.Bang_adrsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_identifiers.
    def visitBang_identifiers(self, ctx:StructurizrParser.Bang_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_extend.
    def visitBang_extend(self, ctx:StructurizrParser.Bang_extendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_impliedRelationships.
    def visitBang_impliedRelationships(self, ctx:StructurizrParser.Bang_impliedRelationshipsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_ref.
    def visitBang_ref(self, ctx:StructurizrParser.Bang_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_script.
    def visitBang_script(self, ctx:StructurizrParser.Bang_scriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_script_body.
    def visitBang_script_body(self, ctx:StructurizrParser.Bang_script_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_var.
    def visitBang_var(self, ctx:StructurizrParser.Bang_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_const.
    def visitBang_const(self, ctx:StructurizrParser.Bang_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_include.
    def visitBang_include(self, ctx:StructurizrParser.Bang_includeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_plugin.
    def visitBang_plugin(self, ctx:StructurizrParser.Bang_pluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bang_plugin_body.
    def visitBang_plugin_body(self, ctx:StructurizrParser.Bang_plugin_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#bangs.
    def visitBangs(self, ctx:StructurizrParser.BangsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#terminology.
    def visitTerminology(self, ctx:StructurizrParser.TerminologyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#terminology_body.
    def visitTerminology_body(self, ctx:StructurizrParser.Terminology_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#users.
    def visitUsers(self, ctx:StructurizrParser.UsersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#users_body.
    def visitUsers_body(self, ctx:StructurizrParser.Users_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#scope.
    def visitScope(self, ctx:StructurizrParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#visibility.
    def visitVisibility(self, ctx:StructurizrParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#themes.
    def visitThemes(self, ctx:StructurizrParser.ThemesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#theme.
    def visitTheme(self, ctx:StructurizrParser.ThemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#branding.
    def visitBranding(self, ctx:StructurizrParser.BrandingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#branding_body.
    def visitBranding_body(self, ctx:StructurizrParser.Branding_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#openCurly.
    def visitOpenCurly(self, ctx:StructurizrParser.OpenCurlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#closeCurly.
    def visitCloseCurly(self, ctx:StructurizrParser.CloseCurlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#instances.
    def visitInstances(self, ctx:StructurizrParser.InstancesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#path.
    def visitPath(self, ctx:StructurizrParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#name.
    def visitName(self, ctx:StructurizrParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#value.
    def visitValue(self, ctx:StructurizrParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#object.
    def visitObject(self, ctx:StructurizrParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#properties.
    def visitProperties(self, ctx:StructurizrParser.PropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#name_value_pair.
    def visitName_value_pair(self, ctx:StructurizrParser.Name_value_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#identifier.
    def visitIdentifier(self, ctx:StructurizrParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#technology.
    def visitTechnology(self, ctx:StructurizrParser.TechnologyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#tag.
    def visitTag(self, ctx:StructurizrParser.TagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#key.
    def visitKey(self, ctx:StructurizrParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#description.
    def visitDescription(self, ctx:StructurizrParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#tags.
    def visitTags(self, ctx:StructurizrParser.TagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#title.
    def visitTitle(self, ctx:StructurizrParser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#url.
    def visitUrl(self, ctx:StructurizrParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#location.
    def visitLocation(self, ctx:StructurizrParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#group.
    def visitGroup(self, ctx:StructurizrParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#group_body.
    def visitGroup_body(self, ctx:StructurizrParser.Group_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#perspective.
    def visitPerspective(self, ctx:StructurizrParser.PerspectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StructurizrParser#keywords.
    def visitKeywords(self, ctx:StructurizrParser.KeywordsContext):
        return self.visitChildren(ctx)



del StructurizrParser